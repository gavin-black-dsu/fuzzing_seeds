
import atheris
import sys

with atheris.instrument_imports():
    import shlex

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    input_str = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        # This is the main function call that we're testing.
        shlex.split(input_str)
    except ValueError:
        # We expect ValueError for some inputs, so it's fine.
        pass
    except Exception as e:
        # Report any other exceptions that are not expected.
        print(f"Unexpected exception: {e}")
        raise e

def main():
    # Initialize Atheris with the fuzz target.
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
