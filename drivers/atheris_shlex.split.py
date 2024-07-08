import atheris
import sys

with atheris.instrument_imports():
    import shlex

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    input_str = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        shlex.split(input_str)
    except ValueError:
        pass
    except Exception as e:
        print(f"Unexpected exception: {e}")
        raise e

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
