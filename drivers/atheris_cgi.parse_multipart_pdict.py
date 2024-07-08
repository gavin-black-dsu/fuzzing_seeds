import atheris
import sys
import io
import cgi
import fcntl

from hypothesis import strategies as st


def TestInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    boundary = fdp.ConsumeString(10)
    content_length = fdp.ConsumeIntInRange(0, 10000)
    
    pdict = {'boundary': boundary.encode('utf-8'), 'CONTENT-LENGTH': content_length}

    try:
        content_type = 'multipart/form-data; boundary=' + boundary
        buffer_length = fdp.ConsumeIntInRange(0, 1000)
        data = fdp.ConsumeBytes(buffer_length)

        stream = io.BytesIO(data) 

        cgi.parse_multipart(stream, pdict)
    except ValueError:
        pass  # Ignore ValueErrors, which are expected for some inputs
    except KeyError:
        pass  # Ignore KeyErrors, this example fuzzes fairly simplistically
    except OverflowError:
        pass  # Avoid crashing on issues like too large integers for the CONTENT-LENGTH


@atheris.instrument_func
def main():
    atheris.Setup(sys.argv, TestInput, enable_python_coverage=True)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
