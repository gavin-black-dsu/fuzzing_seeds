import atheris
import requests
import sys

def TestOneInput(data):
    try:
        decoded_data = data.decode('utf-8', errors='ignore')
        
        param_key = decoded_data[:50]  # Limiting the length of data for fuzzing
        param_value = decoded_data[50:100]  # Limiting the length of data for fuzzing
        
        params = {param_key: param_value}
        response = requests.get(decoded_data,timeout=0.1, params=params)
        
    except (requests.exceptions.RequestException, UnicodeDecodeError):
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    
    atheris.Fuzz()

if __name__ == "__main__":
    main()
