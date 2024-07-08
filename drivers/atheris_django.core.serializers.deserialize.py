import atheris
import sys
import os

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

def TestOneInput(data):
    try:
        objs = deserialize('json', data.decode('utf-8', errors='ignore'))
        for obj in objs:
            pass
    except (ValueError, TypeError, django.core.serializers.base.DeserializationError):
        pass
    except Exception as e:
        print("Unexpected exception:", e)

atheris.Setup(sys.argv, TestOneInput)

if __name__ == "__main__":
    atheris.Fuzz()
