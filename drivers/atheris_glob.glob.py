import atheris
import sys

with atheris.instrument_imports():
    import glob

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    pattern = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        result = glob.glob(pattern)
    except Exception as e:
        print(f"An exception occurred: {e}")

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
