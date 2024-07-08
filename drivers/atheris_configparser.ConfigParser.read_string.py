import atheris
import sys
import configparser

with atheris.instrument_imports():
    pass


def TestOneInput(data):
    try:
        fdp = data.decode("utf-8", errors="ignore")
        
        parser = configparser.ConfigParser()

        parser.read_string(fdp)
    
    except configparser.Error:
        pass
    except UnicodeDecodeError:
        pass
    except Exception as e:
        print(f"Unexpected exception: {e}")
        raise


if __name__ == "__main__":
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()
