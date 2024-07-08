import atheris
import sys
import ast

with atheris.instrument_imports():
    import ast

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    test_string = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        result = ast.literal_eval(test_string)
    except (ValueError, SyntaxError):
        pass
    except Exception as e:
        print(f"Crash with input: {test_string}")
        raise e

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
