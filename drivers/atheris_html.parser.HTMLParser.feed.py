import atheris
import sys

from html.parser import HTMLParser

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    html_data = fdp.ConsumeUnicode(sys.maxsize)

    parser = HTMLParser()
    try:
        parser.feed(html_data)
    except Exception as e:
        pass

atheris.Setup(sys.argv, TestOneInput)

if __name__ == "__main__":
    atheris.Fuzz()
