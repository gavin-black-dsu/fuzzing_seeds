
import atheris
import pygments
from pygments import lexers
import sys

def fuzz_pygments(data):
    try:
        # Fuzz the pygments.lex function with PythonLexer
        pygments.lex(data, pygments.lexers.PythonLexer())
    except Exception as e:
        # Handle the exception
        print("Exception occurred:", e)

def main():
    atheris.Setup(sys.argv, fuzz_pygments)
    atheris.Fuzz()

if __name__ == "__main__":
    main()