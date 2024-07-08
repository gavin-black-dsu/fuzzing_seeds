import atheris
import sys

with atheris.instrument_imports():
    from urllib.parse import parse_qs

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    fuzzed_str = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        result = parse_qs(fuzzed_str)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
