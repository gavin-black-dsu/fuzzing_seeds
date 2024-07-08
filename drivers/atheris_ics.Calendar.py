import atheris
import sys
from ics import Calendar

def TestOneInput(data):
    try:
        Calendar(data.decode("utf-8", errors="ignore"))
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    
    atheris.Fuzz()

if __name__ == "__main__":
    main()
