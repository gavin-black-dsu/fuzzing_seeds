
import atheris
import sys

from email import message_from_string

# Atheris instrumented entry point
@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    # Generate test input for the email parsing function
    email_str = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        # Fuzz email.message_from_string to find vulnerabilities
        msg = message_from_string(email_str)
        
        # Optional: You can add further logic to manipulate or check `msg`
        # For instance, asserting on msg's type or contents
        # This can help in identifying more intricate issues that merely
        # executing the function might not reveal.
    except Exception as e:
        # Optionally, catch specific exceptions if you're interested in
        # particular error conditions or ignore this to just catch crashes.
        pass

def main():
    # Initialize atheris with the fuzz function
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
