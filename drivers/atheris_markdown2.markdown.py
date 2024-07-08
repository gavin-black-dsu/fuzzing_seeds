import atheris
import sys

import markdown2

@atheris.instrument_func
def test_markdown(data):
    try:
        fuzzed_data = data.decode("utf-8", errors="ignore")
        markdown2.markdown(fuzzed_data)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, test_markdown)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
