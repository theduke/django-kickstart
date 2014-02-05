import os

import base
from .base import DATA_DIR

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db', 'db.sqlite3'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# To extend any settings from settings/base.py here's an example:
INSTALLED_APPS = base.INSTALLED_APPS + ()

DEBUG = TEMPLATE_DEBUG = True
TEMPLATE_STRING_IF_INVALID = '<VAR_NONEXISTANT>'
