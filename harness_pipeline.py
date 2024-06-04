import subprocess
import os
import sys
import coverage
import yaml
import re

from datalogger import DataLogger

def find_and_read_most_recent_crash_file(directory_path: str="./") -> str:    
    # Prefix of the files to search for
    prefix = "crash-"
    
    # Find all files in the directory starting with the prefix
    files_with_prefix = [file for file in os.listdir(directory_path) if file.startswith(prefix)]
    
    # Sort these files by their modification time, most recent first
    sorted_files = sorted(files_with_prefix, key=lambda x: os.path.getmtime(os.path.join(directory_path, x)), reverse=True)
    
    # If there are any files, read and return the contents of the most recent one
    if sorted_files:
        most_recent_file = sorted_files[0]
        file_path = os.path.join(directory_path, most_recent_file)
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            contents = file.read()
        return f"Contents of {most_recent_file}:\n{contents}"
    else:
        return "No files found starting with 'crash-' in the specified directory."


    
# Function to process YAML content and create variables
def process_yaml(file_path, func_name):
    # Parse the YAML string
    data = None
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # Dictionary to hold the created variables
    created_variables = {}
    # Process each item in the YAML
    for key, value in data.items():
        #if value is None:
            
        #continue  # or you can assign a default value if needed
        if value is not None and "{" in value and "}" in value:  # Check if there's formatting needed
            # Assuming 'format_map()' can be used safely with local variables.
            # You might need to adjust the source of variables for formatting.
            value_formatted = value.format_map({'func_name':func_name})
            created_variables[key] = value_formatted
        else:
            created_variables[key] = value

    return created_variables

class HarnessPipeline:
    def __init__(self, func_name: str, 
                model_version: str="gpt-3.5-turbo", # 'gpt-3.5-turbo','gpt-4-turbo-preview','claude-3-opus-20240229','claude-instant-1.2'
                temperature: float=1.0,
                test_number:int=0, # For labeling in the dataframe for repeated trials
                max_iterations: int=10, # Number of attempts the LLM gets to update the harness
                conda_env: str="amira", # Conda environment to run harness in
                max_len: int=500, # Maximum length of the inputs to generate
                num_runs: int=100, # Number of runs to use to see if the harness is valid (does not error out immediately)
                max_revisions: int=3, # Number of times each upgrade/intrument update can try
                harness_runs: int=5, # Number of times to test the generated harness (harness_runs*num_profiling_runs)
                num_profiling_runs: int=100_000, # Number of runs for generating metrics from the harness
                use_docs: bool=True # Retrieve and send documentation
                ):
        # We generate an "Initial" harness then "Upgrade" it and finally "Instrument" it
        # We track each of these as separate events in their own dataframes
        self.stage = "Initial"
        
        self.use_docs = use_docs
        self.func_name = re.sub(r'\(.*?\)', '', func_name)
        self.model_version = model_version
        self.temperature = temperature
        self.max_iterations = max_iterations
        self.test_number = test_number
        
        self.conda_env = conda_env
        self.max_len = max_len
        self.num_runs = num_runs
        self.harness_runs = harness_runs
        self.num_profiling_runs = num_profiling_runs

        self.max_revisions = max_revisions
        self.update_save_name()
        
    def update_save_name(self):
        self.save_filename =  f"{self.model_version}_{self.func_name}_{self.stage}_{self.test_number}"
        
    def add_trial_data(self):
        DataLogger.add_data('Temperature', self.temperature)
        DataLogger.add_data('Model', self.model_version)
        DataLogger.add_data('Stage', self.stage)
        DataLogger.add_data('Function', self.func_name)
        DataLogger.add_data('Max Iterations', self.max_iterations)

    
    def test_with_corpora(self, simple_corpus, complex_corpus, file_name, harness):
        self.stage = f"{self.stage} with Corpora"
        self.update_save_name()

        avg = 0.0
        if simple_corpus:  
            avg, _ = self.test_harness(file_name, corpus_location="./simple_corpus", finish_df=False)
            
        if complex_corpus: 
            avg_complex, _ = self.test_harness(file_name, corpus_location="./complex_corpus", finish_df=False)
            if avg_complex > avg: avg = avg_complex
            
        if simple_corpus and complex_corpus: 
            avg_merge = self.test_harness(file_name, corpus_location="./merge_corpus", finish_df=False)
            if avg_merge > avg: avg = avg_merge
        DataLogger.create_dataframe(f"harness_test_{self.save_filename}")
        DataLogger.clear() # New dataframe for the next testing
        return avg
        
    def test_harness(self, file_name, instrument_output=None, corpus_location=None, finish_df=True, harness=None):
        # If we are given just the harness code make a temporary file
        if harness is not None and file_name is None:
            file_name = 'tmp_harness.py'
            with open(file_name, 'w') as file:
                file.write(harness)
        
        min_percent = 100
        max_percent = 0
        average_percent = 0
        average_percent_count = 0
        
        # If we found a good harness get coverage over num_profiling_runs
        if file_name is not None: 
            for i in range(self.harness_runs):
                # Delete coverage if it exists
                if os.path.exists(".coverage"): os.remove(".coverage")

                self.add_trial_data()
                DataLogger.add_data('run', i)
                class_name = self.func_name.split(".")[0] # Extract the class from the full function name 
                command = [ "conda", "run", "-n", self.conda_env, "coverage", "run", f"--source={class_name}", file_name ]
                
                # We have a supplied corpus in a directory
                if corpus_location is not None:
                    corpus_name = corpus_location[2:-len("_corpus")].capitalize()
                    print(f"Corpus Name: {corpus_name}")
                    DataLogger.add_data('Corpus', corpus_name)
                    command.append(corpus_location)
                else:
                    DataLogger.add_data('Corpus', None)
                
                # Switches for atheris itself that come after the filename and possible corpus
                command.append(f"-max_len={self.max_len}")
                command.append(f"-atheris_runs={self.num_profiling_runs}")
                # Log them
                DataLogger.add_data('Max Length', self.max_len)
                DataLogger.add_data('Number of Runs', self.num_profiling_runs)
    
                # We tried to instrument the binary to capture files
                if instrument_output is not None:
                    directory_path = f"{instrument_output}_{self.test_number}"
                    os.makedirs(directory_path, exist_ok=True)
                    command.append(f"-artifact_prefix={directory_path}/")
                
                joined_command = " ".join(command)
                print(f"Command: {joined_command}")
                DataLogger.add_data('command', joined_command)
                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if result.returncode != 0:
                    print("Encountered error")
                    DataLogger.add_data('error', f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}\n{find_and_read_most_recent_crash_file()}")
                    with open("run_report.txt", 'w') as file:
                        file.write(f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}\n{find_and_read_most_recent_crash_file()}")
                else:
                    DataLogger.add_data('error', None)

                cov = coverage.Coverage()
                cov.load()
                cov.get_data()
                percent = 0
            
                try:
                    percent = cov.report(file=open(os.devnull, 'w'))
                except coverage.exceptions.NoDataError: # No coverage generated, indicating a likely error
                    pass
                # Track min/max for actual values
                if percent > 0:
                    if percent < min_percent: min_percent = percent
                    if percent > max_percent: max_percent = percent
                average_percent += percent
                average_percent_count += 1
                
                print(f"Coverage: {percent:0.2f}%")
                DataLogger.add_data('coverage', percent)
                DataLogger.finish_row()
        else: # Failed, save 0 coverage
            self.add_trial_data()
            DataLogger.add_data('run', 0)
            DataLogger.add_data('command', "N/A")
            DataLogger.add_data('error', None) 
            DataLogger.add_data('coverage', 0)
            DataLogger.finish_row()
            
        if finish_df: # In cases where testing corpora we often want to keep in same file
            DataLogger.create_dataframe(f"harness_test_{self.save_filename}")
            DataLogger.clear() # New dataframe for the next testing
        
        if average_percent_count > 0:
            average_percent /= average_percent_count
        max_diff = max_percent - min_percent
        if max_diff < 0: max_diff = 0
        return average_percent, max_diff
