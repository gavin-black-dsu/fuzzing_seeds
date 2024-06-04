import atheris
import json
import geojson
import sys

def TestOneInput(data):
    try:
        geojson.loads(data)
    except (json.JSONDecodeError, ValueError):  # Handle ValueError if it occurs
        pass

atheris.Setup(sys.argv, TestOneInput)

atheris.Fuzz()