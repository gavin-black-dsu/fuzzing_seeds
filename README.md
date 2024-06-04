# Atheris Coverage with LLM Seeds

## Description
This project is a comprehensive toolkit for fuzzing Python functions using the Atheris tool. It includes a large collection of LLM-generated inputs for testing and a Jupyter notebook for analyzing coverage across these inputs.

## Components

### Jupyter Notebooks
- **run_driver.ipynb**: The primary notebook for executing fuzzing drivers with the provided seed corpora. It collects and displays coverage results.

### Python Scripts
- **harness_pipeline.py**: Orchestrates the execution of Atheris fuzzers for a specified number of trials.
- **datalogger.py**: Generates dataframes to log and analyze the fuzzing results.
- **seed_data_mapper.py**: Maps driver names to their corresponding original function definitions for detailed logging and result analysis.

### Directories
- **drivers/**: Contains Atheris fuzzing drivers for Python libraries, focusing on internet protocols and input handling.
- **corpora/**: Houses over 38,000 seeds generated for the drivers from various models including ChatGPT-3.5, ChatGPT-4, Claude-Opus, Claude-Instant, and Gemini Pro 1.0.
- **results/**: Stores raw results in both HTML and pandas dataframe formats from the coverage experiments.

## Setup and Installation
To set up and run this project, follow these steps:
1. Clone the repository to your local machine.
2. Create a virtual environment and activate it:
```
python -m venv env
source env/bin/activate # On Windows use env\Scripts\activate
```
3. Install the required dependencies: `pip install -r requirements.txt`
4. Navigate to the project directory and launch Jupyter Notebook
5. Open `run_driver.ipynb` and execute the cells to start fuzzing.

## Usage
To use the fuzzing drivers, follow the steps in `run_driver.ipynb`. The notebook will guide you through the process of loading seed data, running the fuzzers, and collecting coverage data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
