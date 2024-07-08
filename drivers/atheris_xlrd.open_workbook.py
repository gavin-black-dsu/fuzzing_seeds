import atheris
import xlrd
import sys

def fuzz_xlrd_open_workbook(data):
    try:
        if data is None:
            return
        if isinstance(data, str):
            xlrd.open_workbook(file_contents=data.encode())
        else:
            xlrd.open_workbook(file_contents=data)
    except (xlrd.XLRDError, TypeError) as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_xlrd_open_workbook)
    atheris.Fuzz()

if __name__ == "__main__":
    main()

