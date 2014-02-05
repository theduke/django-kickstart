#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    # Extend path with apps and library directories.
    sys.path.append('apps')
    sys.path.append('lib')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
