import atheris
import sys

from email.utils import parseaddr
from hypothesis import strategies as st, given, settings

def TestOneInput(data):
    try:
        fuzzed_string = data.decode("utf-8", errors="ignore")
        parseaddr(fuzzed_string)
    except UnicodeDecodeError:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
