import atheris
import sys

with atheris.instrument_imports():
    from urllib.parse import parse_qsl

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    fuzz_string = fdp.ConsumeUnicode(sys.maxsize)

    try:
        result = parse_qsl(fuzz_string)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
