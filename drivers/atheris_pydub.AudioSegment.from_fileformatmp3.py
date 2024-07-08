import atheris
import io
import pydub
import sys

def fuzz_test(data):
    try:
        audio_segment = pydub.AudioSegment.from_file(io.BytesIO(data), format='mp3')
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_test)
    atheris.Fuzz()

if __name__ == "__main__":
    main()

