
import atheris
import io
import mido
import sys

def fuzz_midi_file(data):
    try:
        mido.MidiFile(file=io.BytesIO(data))
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_midi_file)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
