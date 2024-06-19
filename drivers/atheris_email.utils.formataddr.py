
# fuzz_formataddr.py
import atheris
import sys

from email.utils import formataddr
import sys

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    name = fdp.ConsumeString(sys.maxsize)
    address = fdp.ConsumeString(sys.maxsize)

    # We are fuzzing the formataddr function with a tuple of the name and address.
    try:
        formatted_address = formataddr((name, address))
        # You might want to do some additional checks on formatted_address here
    except Exception as e:
        # Optionally catch and log exceptions, or pass to handle unexpected issues
        if not isinstance(e, (ValueError, UnicodeEncodeError)):
            raise e

def main():
    # You must initialize Atheris before the fuzzer starts
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
