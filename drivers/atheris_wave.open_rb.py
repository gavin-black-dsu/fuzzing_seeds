import atheris
import wave
import io
import sys

def fuzz_wave_open(data):
    try:
        wave.open(io.BytesIO(data), 'rb')
    except Exception as e:
        pass

def initialize():
    atheris.Setup(sys.argv, fuzz_wave_open)

if __name__ == "__main__":
    initialize()
    atheris.Fuzz()
