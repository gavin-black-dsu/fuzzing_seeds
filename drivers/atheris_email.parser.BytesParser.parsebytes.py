import atheris
import sys
import email.parser

from email.parser import BytesParser

def fuzz_parsebytes(data):
    try:
        BytesParser().parsebytes(data)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_parsebytes)

    atheris.Fuzz()

if __name__ == "__main__":
    main()
