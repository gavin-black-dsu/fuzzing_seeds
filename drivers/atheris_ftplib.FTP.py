import atheris
import sys
import ftplib
import io


with atheris.instrument_imports():
    pass

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    hostname = fdp.ConsumeUnicode(sys.maxsize)

    try:
        dummy_file = io.BytesIO()
        
        ftp = ftplib.FTP(hostname, timeout=0.5)


        ftp.quit()
    except Exception as e:
        print(f"Caught an exception: {e}")
    
    finally:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
