import atheris
import sys
import io
import rarfile

with atheris.instrument_imports():
    pass

def TestOneInput(data):
    try:
        with rarfile.RarFile(io.BytesIO(data)) as rf:
            for f in rf.infolist():
                try:
                    _ = rf.read(f)  # Consider this extension to increase interaction with the rarfile module.
                except rarfile.Error:
                    pass
    except rarfile.Error:
        pass
    except Exception as e:
        print(f"Caught unexpected exception: {e}")

atheris.Setup(sys.argv, TestOneInput)

if __name__ == "__main__":
    atheris.Fuzz()
