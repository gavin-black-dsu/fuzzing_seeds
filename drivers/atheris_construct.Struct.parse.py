import atheris
import sys
from construct import Struct, Int32ul

def fuzz_construct(data):
    try:
        if len(data) < 4:
            raise ValueError("Input data length less than 4 bytes")
        
        schema = Struct("field" / Int32ul)
        
        result = schema.parse(data)
        
    except ValueError as ve:
        if "stream read less than specified amount" in str(ve) or "Input data length less than 4 bytes" in str(ve):
            pass
        else:
            raise
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_construct)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
