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
django-admin.py startproject --template="/home/theduke/Coding/projects/django-kickstart" --extension="py,html,gitignore,md,txt"

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

3) Create local settings file.

ln -s app/apps/{{ project_name }}/settings/settings-dev.py app/apps/{{ project_name }}/settings/local.py

4) Create sqlite database for development.

app/manage.py syncdb
app/manage.py migrate


) Start building your awesome site.

Updating bootstrap-sass
-----------------------

After updating bootstrap-sass, you need to copy the javascript and font assets.

cd to root (dir with this readme file in it)
cp -r $(bundle show bootstrap-sass)/vendor/assets/fonts/* app/apps/{{ project_name }}/static/fonts/
cp -r $(bundle show bootstrap-sass)/vendor/assets/javascripts/* app/apps/{{ project_name }}/static/js/
