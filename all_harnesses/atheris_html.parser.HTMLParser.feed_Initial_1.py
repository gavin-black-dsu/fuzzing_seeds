
import atheris
import sys

# Import the HTMLParser module
from html.parser import HTMLParser

# Specify the fuzz target
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    html_data = fdp.ConsumeUnicode(sys.maxsize)

    # Initialize HTMLParser
    parser = HTMLParser()
    try:
        # Feed the fuzzed data to the parser
        parser.feed(html_data)
    except Exception as e:
        # You might want to log or handle certain exceptions differently
        pass

# Setup for fuzzing
atheris.Setup(sys.argv, TestOneInput)

# Fuzz!
if __name__ == "__main__":
    atheris.Fuzz()
