import atheris
import io
import sys
import sunau

def fuzz_test(data):
    try:
        sunau.open(io.BytesIO(data), 'rb')
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_test)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
