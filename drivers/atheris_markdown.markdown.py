import sys
import atheris
import markdown

def TestOneInput(data):
    try:
        markdown.markdown(data)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
