
import atheris
import sys

import html5lib

# Fuzzing function
@atheris.instrument_func # Instrument this function for coverage.
def TestOneInput(data):
    try:
        # Attempt to parse the fuzzed data.
        html5lib.parse(data)
    except Exception as e:
        # We catch all exceptions since we're looking for crashes,
        # but depending on your test's intent, you might want to handle them differently.
        pass

def main():
    # Setup Atheris with the entry point (fuzzer test) to execute.
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
