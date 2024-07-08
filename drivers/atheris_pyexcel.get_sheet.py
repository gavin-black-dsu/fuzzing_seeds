import atheris
import pyexcel
import sys

def fuzz(data):
    try:
        sheet = pyexcel.get_sheet(file_type='csv', file_content=data)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
