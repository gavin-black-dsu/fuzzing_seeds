import atheris
import sys

from email import message_from_string

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    email_str = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        msg = message_from_string(email_str)
        
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
