
import atheris
import sys
import plistlib
from typing import Any
import io
import ast  # Import the ast module for safe evaluation

with atheris.instrument_imports():
    pass

def TestOneInput(data: bytes) -> None:
    try:
        input_str = data.decode("utf-8")
        # Use ast.literal_eval for safe evaluation of input data
        input_data = ast.literal_eval(input_str)
        
        # Check if input_data is of a type plistlib can serialize
        if not isinstance(input_data, (dict, list, tuple, bool, int, float, str, bytes)):
            return
        
        # Serialize the data using plistlib.dumps
        plist_bytes = plistlib.dumps(input_data)
        
        # Optionally, deserialize the data to complete the fuzzing cycle
        loaded_data = plistlib.loads(plist_bytes)
        
    except (ValueError, SyntaxError, UnicodeDecodeError, plistlib.InvalidFileException, OverflowError):
        # OverflowError included for completeness, in case the evaluated data leads to numbers too large for plistlib
        # Ignore exceptions, as malformed inputs are part of the fuzzing process
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
