import atheris
import sys
import plistlib
from typing import Any
import io
import ast

with atheris.instrument_imports():
    pass

def TestOneInput(data: bytes) -> None:
    try:
        input_str = data.decode("utf-8")
        input_data = ast.literal_eval(input_str)
        
        if not isinstance(input_data, (dict, list, tuple, bool, int, float, str, bytes)):
            return
        
        plist_bytes = plistlib.dumps(input_data)
        
        loaded_data = plistlib.loads(plist_bytes)
        
    except (ValueError, SyntaxError, UnicodeDecodeError, plistlib.InvalidFileException, OverflowError):
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
