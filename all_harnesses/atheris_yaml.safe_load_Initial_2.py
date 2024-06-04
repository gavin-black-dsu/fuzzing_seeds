import atheris
import yaml
import sys

def TestOneInput(data):
    try:
        yaml.safe_load(data)
    except Exception as e:
        pass

def main():
    # Initialize Atheris
    atheris.Setup(sys.argv, TestOneInput)

    # Fuzz indefinitely
    atheris.Fuzz()

if __name__ == "__main__":
    main()
    
# Ensure to import sys module in order to resolve 'sys' is not defined error.