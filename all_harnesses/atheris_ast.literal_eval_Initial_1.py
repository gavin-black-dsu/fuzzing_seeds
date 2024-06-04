
import atheris
import sys
import ast

with atheris.instrument_imports():
    # You can include modules that ast.literal_eval interacts with,
    # or any module you think whose interaction with ast.literal_eval might reveal bugs.
    import ast

# Fuzzing function to test ast.literal_eval
@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    test_string = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        # This is where we call ast.literal_eval with the fuzzed input
        result = ast.literal_eval(test_string)
    except (ValueError, SyntaxError):
        # These exceptions are expected for invalid input,
        # so we catch them and don't treat them as failures.
        pass
    except Exception as e:
        # If any other exception occurs, print the input that caused it.
        # This indicates a bug that needs investigation.
        print(f"Crash with input: {test_string}")
        raise e

# Setup Atheris
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
