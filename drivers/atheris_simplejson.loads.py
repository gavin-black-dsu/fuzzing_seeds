import atheris
import simplejson
import sys

def fuzz_data(data):
    try:
        simplejson.loads(data, encoding='utf-8', strict=False)
    except (simplejson.JSONDecodeError, UnicodeDecodeError):
        pass

def main():
    atheris.Setup(sys.argv, fuzz_data)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
