import atheris
import sys

import smtplib
import socket

def fuzz_smtp_init(data):
    fdp = atheris.FuzzedDataProvider(data)

    hostname = fdp.ConsumeString(100)
    port = fdp.ConsumeIntInRange(0, 65535)

    try:
        smtp_obj = smtplib.SMTP(host=hostname, port=port, timeout=10)
    except (smtplib.SMTPException, socket.timeout, OSError) as e:
        print(f"Caught expected exception: {e}")
    except Exception as unexpected_e:
        print(f"Caught unexpected exception: {unexpected_e}")
        raise unexpected_e

def TestOneInput(data):
    fuzz_smtp_init(data)

atheris.Setup(sys.argv, TestOneInput)

if __name__ == "__main__":
    atheris.Fuzz()
