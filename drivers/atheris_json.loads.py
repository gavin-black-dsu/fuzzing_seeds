
import atheris
import json
import sys

def TestOneInput(data):
    try:
        json.loads(data)
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass

atheris.Setup(sys.argv, TestOneInput)

if __name__ == "__main__":
    atheris.Fuzz()
