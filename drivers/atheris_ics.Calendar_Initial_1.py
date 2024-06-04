
import atheris
import sys
from ics import Calendar

# Fuzz target that will try to parse the data it is fed.
def TestOneInput(data):
    try:
        # Attempt to parse the data as an iCalendar string
        Calendar(data.decode("utf-8", errors="ignore"))
    except Exception as e:
        # You can choose to log exceptions or specific conditions you're hunting for
        pass

def main():
    # Initialize Atheris with no arguments
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    
    # Run Atheris
    atheris.Fuzz()

if __name__ == "__main__":
    main()
