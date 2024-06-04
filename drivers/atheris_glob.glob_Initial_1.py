
import atheris
import sys

with atheris.instrument_imports():
    import glob

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    pattern = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        # Attempt to glob files based on the fuzzed pattern.
        result = glob.glob(pattern)
        print("Globbed: ", result)  # You might want to comment this out to avoid flooding stdout.
    except Exception as e:
        print(f"An exception occurred: {e}")
        # Optionally, re-raise exceptions you consider as vulnerabilities or bugs.
        # raise e

def main():
    # Setup Atheris fuzzer
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
