import atheris
import sys

from bs4 import BeautifulSoup

with atheris.instrument_imports():
    pass


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    html_data = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        BeautifulSoup(html_data, 'html.parser')
    except Exception as e:
        print(f"Caught exception: {e}")
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)

    atheris.Fuzz()

if __name__ == "__main__":
    main()
