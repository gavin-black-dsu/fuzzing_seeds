import atheris
import yaml
import sys

def fuzz_test(data):
    try:
        yaml.load(data, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_test)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
