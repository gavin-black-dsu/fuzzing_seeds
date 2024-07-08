import atheris
import sys

from email.parser import Parser

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    email_data = fdp.ConsumeString(sys.maxsize)

    try:
        parser = Parser()
        parser.parsestr(email_data)
    except Exception as e:
        
        print(f"Caught an exception: {e}")

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
