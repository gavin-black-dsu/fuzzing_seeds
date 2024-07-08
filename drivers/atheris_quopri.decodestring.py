import atheris
import sys
import quopri
import io

from hypothesis import strategies as st, given, settings, Phase

@given(st.binary())
@settings(phases=[Phase.generate], deadline=None)
def test_quopri_decoding(data):
    try:
        decoded_data = quopri.decodestring(data)
        
    except Exception as e:
        pass


def main():
    atheris.Setup(sys.argv, test_quopri_decoding.hypothesis.fuzz_one_input)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
