import atheris
import exrex
import sys

def TestOne(data):
    try:
        input_str = data.decode('utf-8')
    except UnicodeDecodeError:
        return

    try:
        if input_str.strip() == "":
            return  # Skip empty input strings
        result = exrex.getone(input_str)
    except Exception as e:
        print("Exception occurred for input: {}".format(input_str))

atheris.Setup(sys.argv, TestOne)
atheris.Fuzz()
