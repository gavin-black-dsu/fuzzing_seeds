import atheris
import sys
import toml

with atheris.instrument_imports():
    pass

@atheris.instrument_func
def TestOneInput(data):
    try:
        toml_string = data.decode("utf-8")
        toml.loads(toml_string)
    except (toml.TomlDecodeError, UnicodeDecodeError):
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
