
import atheris
import sys
import quopri
import io

from hypothesis import strategies as st, given, settings, Phase

@given(st.binary())
@settings(phases=[Phase.generate], deadline=None)
def test_quopri_decoding(data):
    # Wrap the operation in try-except to manage potential exceptions
    try:
        decoded_data = quopri.decodestring(data)
        
        # If the decoding is successful, you might want to perform additional
        # correctness checks, such as comparing the re-encoded output if suitable.
    except Exception as e:
        # It's a good idea to catch and log exceptions, so you understand what went wrong.
        # However, in fuzzing, exceptions are often expected and can even be what you're looking for.
        pass


def main():
    # Initialize Atheris with the fuzzing arguments and your test function
    atheris.Setup(sys.argv, test_quopri_decoding.hypothesis.fuzz_one_input)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
