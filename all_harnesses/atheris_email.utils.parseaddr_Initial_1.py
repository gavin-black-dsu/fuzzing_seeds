
import atheris
import sys

from email.utils import parseaddr
from hypothesis import strategies as st, given, settings

# Fuzz Target that takes bytes input
def TestOneInput(data):
    try:
        # Convert fuzzer data to string, as parseaddr expects a string.
        fuzzed_string = data.decode("utf-8", errors="ignore")
        # Pass the fuzzed string to the target function
        parseaddr(fuzzed_string)
    except UnicodeDecodeError:
        # In the case of a decoding error, we'll just pass since the input is invalid,
        # but you might want to log this or handle it differently depending on your goals.
        pass

# Setup Atheris with entry point (TestOneInput) and any command line arguments
def main():
    # Use atheris.Setup() with the entry point and have atheris.Fuzz() to start the fuzzer
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
