#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Make it possible to run from any directory.
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    sys.path.append('apps')
    sys.path.append('lib')

    # Now add virtualenv site-packages path.
    from {{ project_name }} import settings
    sys.path.append(os.path.join(settings.VIRTENV_DIR, settings.VIRTENV_PACKAGE_DIR))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
