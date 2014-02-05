DJANGO-KICKSTART
================

This project template helps you to kickstart your new django project,
by providing a better, more comprehensive setup that allows you to get
going right away.


How to use:
-----------

Steps:

1) Start the new project.
django-admin.py startproject --template="" --extension="py,html,gitignore" --domain="YOURDOMAIN.COM" PROJECTNAME

2) Create virtualenv.

cd PROJECT
# Remove stub pyenv file.
rm -r pyenv
# Create virtualenv with name pyenv.
virtualenv pyenv
# Activate the new virtualenv.
. pyenv/bin/activate

3) Install requirements.

pip install -r app/requirements/development.txt

4) Create sqlite database for development.

app/manage.py syncdb
app/manage.py migrate


) Start building your awesome site.
