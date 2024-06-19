
import atheris
import sys
import os

# Inline Django settings for fuzzing
from django.conf import settings
settings.configure(
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    USE_TZ=True,
)

import django
django.setup()

from django.core.serializers import deserialize

# Fuzz target function
def TestOneInput(data):
    try:
        # Use bytes data as input for deserialization
        objs = deserialize('json', data.decode('utf-8', errors='ignore'))
        for obj in objs:
            # Potential interaction with deserialized objects
            pass
    except (ValueError, TypeError, django.core.serializers.base.DeserializationError):
        # Expected exceptions for invalid input, ignore
        pass
    except Exception as e:
        # Log unexpected exceptions
        print("Unexpected exception:", e)

# Atheris setup
atheris.Setup(sys.argv, TestOneInput)

if __name__ == "__main__":
    # Start fuzzing
    atheris.Fuzz()
