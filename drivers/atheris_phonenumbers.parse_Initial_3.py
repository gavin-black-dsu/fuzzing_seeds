import atheris
import phonenumbers
import sys

def FuzzOneInput(data):
    try:
        data_str = data.decode('utf-8', 'ignore')  # Ignore encoding errors
        parsed_number = phonenumbers.parse(data_str, 'US')
        if parsed_number is not None:
            print(f"Parsed phone number: {parsed_number}")
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error parsing phone number: {e}")

atheris.Setup(sys.argv, FuzzOneInput)
atheris.Fuzz()