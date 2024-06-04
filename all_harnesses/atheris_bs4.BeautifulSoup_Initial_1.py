
import atheris
import sys

# Import the library function you wish to fuzz
from bs4 import BeautifulSoup

with atheris.instrument_imports():
    # Place any additional imports here that needs to be instrumented by Atheris
    pass


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    html_data = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        # Call the function with the fuzzed data
        BeautifulSoup(html_data, 'html.parser')
    except Exception as e:
        # Usually, you handle expected exceptions that are not indicative of bugs,
        # or you assert specific error conditions that should not occur.
        # Unexpected crashes or behaviors are what we want Atheris to discover.
        print(f"Caught exception: {e}")
        pass # In a real fuzzing scenario, you might want to remove or customize this part.

# Entry point for the fuzzer
def main():
    # Initialize Atheris with the entry point for fuzzing (TestOneInput function)
    atheris.Setup(sys.argv, TestOneInput)

    # Start the fuzzing process
    atheris.Fuzz()

if __name__ == "__main__":
    main()
