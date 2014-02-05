""" Settings for {{ project_name }} """

from .base import *
try:
    from .local import *
except ImportError, exc:
    raise Exception('Could not find settings/local.py settings file!')
