
import atheris
import sys

# Import the markdown2 library
import markdown2

# Define the fuzz test function
@atheris.instrument_func
def test_markdown(data):
    try:
        # Convert the fuzzed data into a string (if it's not already)
        fuzzed_data = data.decode("utf-8", errors="ignore")
        # Pass the fuzzed string data to the markdown function
        markdown2.markdown(fuzzed_data)
    except Exception as e:
        # Handle exceptions that are expected and ignore them
        # For unexpected exceptions, you might want to log them or handle differently
        pass

# Setup Atheris with the fuzz test function
def main():
    # Needed for Atheris instrumentation to cover the code in Python-only modules
    atheris.Setup(sys.argv, test_markdown)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
