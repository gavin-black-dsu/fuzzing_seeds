import atheris
import yaml
import sys

def TestOneInput(data):
    try:
        yaml.safe_load(data)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)

    atheris.Fuzz()

if __name__ == "__main__":
    main()
    
