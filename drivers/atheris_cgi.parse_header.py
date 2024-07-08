import atheris
import sys
import cgi

with atheris.instrument_imports():
    pass


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    header_string = fdp.ConsumeUnicode(sys.maxsize)

    try:
        result = cgi.parse_header(header_string)
    except Exception as e:
        pass


atheris.Setup(sys.argv, TestOneInput)

atheris.Fuzz()
