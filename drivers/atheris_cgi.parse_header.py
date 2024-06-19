
import atheris
import sys
import cgi

with atheris.instrument_imports():
    # Import any additional modules that might be relevant or used alongside cgi.parse_header
    pass


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    header_string = fdp.ConsumeUnicode(sys.maxsize)

    try:
        # Here we call cgi.parse_header with the fuzzed data
        result = cgi.parse_header(header_string)
        # Optionally, you can add assertions or checks to see if the output is as expected. 
        # However, for just fuzzing, catching exceptions might be sufficient.
    except Exception as e:
        # You might want to log or handle specific exceptions differently
        pass


# Set up Atheris to call the TestOneInput function.
atheris.Setup(sys.argv, TestOneInput)

# Start the fuzzer
atheris.Fuzz()
