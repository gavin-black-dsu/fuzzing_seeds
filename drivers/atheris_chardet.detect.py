import atheris
import chardet
import sys

def TestOneInput(data):
    try:
        result = chardet.detect(data)
    except UnicodeDecodeError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
