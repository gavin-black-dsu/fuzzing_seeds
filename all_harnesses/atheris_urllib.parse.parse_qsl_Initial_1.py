
import atheris
import sys

with atheris.instrument_imports():
    from urllib.parse import parse_qsl

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    # Generate a random string from the fuzz data.
    fuzz_string = fdp.ConsumeUnicode(sys.maxsize)

    try:
        # Attempt to parse the fuzzed string.
        result = parse_qsl(fuzz_string)
        # Optionally, inspect the result or look for specific anomalies.
        # print(result)
    except Exception as e:
        # Optionally handle known exceptions or unexpected behaviors.
        # print(f"Caught an exception: {e}")
        pass

def main():
    # Setup fuzzing arguments and run the fuzzer.
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
