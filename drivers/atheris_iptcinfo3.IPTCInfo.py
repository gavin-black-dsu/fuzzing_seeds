import atheris
import iptcinfo3
import io
import sys

def fuzz_iptcinfo(data):
    try:
        iptcinfo3.IPTCInfo(io.BytesIO(data))
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_iptcinfo)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
    
