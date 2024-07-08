import atheris
import sys

import tablib

@atheris.instrument_func
def test_tablib_import_set(data):
    try:
        data_str = data.decode("utf-8", errors="ignore")
        tablib.import_set(data_str, format='csv')
    except Exception as e:
        print(f"Caught exception: {e}")

def main():
    atheris.Setup(sys.argv, test_tablib_import_set)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
