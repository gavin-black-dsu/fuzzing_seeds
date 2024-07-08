import atheris
import sys

import html5lib

@atheris.instrument_func # Instrument this function for coverage.
def TestOneInput(data):
    try:
        html5lib.parse(data)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
