import atheris
import pandas as pd
import sys
import io

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    csv_data = fdp.ConsumeString(sys.maxsize)
    
    try:
        df = pd.read_csv(io.StringIO(csv_data))
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
