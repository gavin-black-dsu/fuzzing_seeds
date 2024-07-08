import atheris
import sys

from email.utils import formataddr
import sys

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    name = fdp.ConsumeString(sys.maxsize)
    address = fdp.ConsumeString(sys.maxsize)

    try:
        formatted_address = formataddr((name, address))
    except Exception as e:
        if not isinstance(e, (ValueError, UnicodeEncodeError)):
            raise e

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
