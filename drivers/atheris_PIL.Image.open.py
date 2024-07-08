import atheris
import PIL.Image
import io
import sys

def TestOneInput(data):
    try:
        image = PIL.Image.open(io.BytesIO(data))
    except Exception as e:
        pass

if __name__ == "__main__":
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz() 
