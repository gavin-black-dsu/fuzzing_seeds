import atheris
import sys

from email.utils import parsedate
from hypothesis import strategies as st, given

@atheris.instrument_func
def test_parsedate(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    date_str = fdp.ConsumeUnicode(sys.maxsize)
    
    try:
        result = parsedate(date_str)
        
        
    except Exception as e:
        print(f"Exception caught: {e}")

def main():
    atheris.Setup(sys.argv, test_parsedate)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
