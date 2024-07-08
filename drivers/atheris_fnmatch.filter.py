import atheris
import fnmatch
import sys

def fuzz_test(data):
    try:
        fnmatch.filter(['file1.txt', 'file2.txt'], data)
    except:
        pass

def initialize():
    atheris.Setup(sys.argv, fuzz_test)

if __name__ == "__main__":
    initialize()
    atheris.Fuzz()
