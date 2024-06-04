
import atheris
import requests
import sys

def TestOneInput(data):
    try:
        # Decode the input data as UTF-8
        decoded_data = data.decode('utf-8', errors='ignore')
        
        # Fuzz the params dictionary key and value
        param_key = decoded_data[:50]  # Limiting the length of data for fuzzing
        param_value = decoded_data[50:100]  # Limiting the length of data for fuzzing
        
        # Send the request using the fuzzed data
        params = {param_key: param_value}
        response = requests.get(decoded_data,timeout=0.1, params=params)
        
    except (requests.exceptions.RequestException, UnicodeDecodeError):
        pass

def main():
    # Setup Atheris for fuzzing
    atheris.Setup(sys.argv, TestOneInput)
    
    # Fuzz the requests.get function with input data
    atheris.Fuzz()

if __name__ == "__main__":
    main()
