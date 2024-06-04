
# Updated code:
import atheris
import simplejson
import sys

# Fuzzing harness function
def fuzz_data(data):
    try:
        simplejson.loads(data, encoding='utf-8', strict=False)
    except (simplejson.JSONDecodeError, UnicodeDecodeError):
        pass

# Main function to setup Atheris and start fuzzing
def main():
    atheris.Setup(sys.argv, fuzz_data)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
