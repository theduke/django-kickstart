DJANGO-KICKSTART
================

This tool helps you to kickstart your new django project,
by providing a better, more comprehensive setup that allows you to get
going right away, and saves your precious time by automating tedious tasks.

The template used provides a setup **based on current best practices**, and makes
starting a new project a breeze.

After running django-kickstart, you will have a functional django setup with it's
**own virtualenv** preconfigured, with bower packages fetched and **jQuery, modernizr**,
and some **IE8 polyfills** ready and included in the base.html template,
**SASS with Compass and Twitter Bootstrap** (SASS port) ready,
 all relevant settings configured (including **django-allauth**), and a **development sqlite database ready to use**.


Quickstart:
-----------

`pip install django-kickstart`

`django-kickstart mynewproject`

`cd mynewproject/app`

`export ENV=dev`

`./manage.py runserver`

Note that for manage.py to work, you need to set the environment variable ENV
to dev.

(type `django-kickstart -h` for all options)


Features:
--------

(for more details check About section)

* SASS + Compass
* Twitter Bootstrap
* jQuery + Modernizr
* IE Polyfills (for css3, media queries, html5 tags)

* Bower with django-bower for frontend package management
* django-pipeline for asset management
* Good directory structure
* Django setup with environment variables

* Auto-create a git repo and do an intial commit
* South for schema management


Directory Structure
-------------------

app/ - the django project

  apps/ - containts your custom django apps

  data/

    db/ - contains development sqlite databases

    fixtures/ - contains database fixtures

    lib/ - place to put external, contributed django apps or python modules that are not available from PyPi

    public/ - only this dir needs to be publicly accessible

      media/ - Uploaded media

      static/ - static files

    requirements/ - contains package requirements for pip, separated by environment

bin/ - various (non-django/python) scripts (bash,...) related to the project

conf/ - Config files or templated you need, for example apache virtual host or other server configs

docs/ - documentation

pyenv/ - A custom virtualenv for your project. This will be automatically
         created, and all dependencies will be downloaded


What and why:
-------------

*  Modern and advanced CSS development with a setup for SASS, Compass, and
   optionally Bootstrap (the Bootstrap SASS port).
   Compass will require a setup of ruby and the gems specified in the GEMFILE
   of the newly created project, but if you don't want to use SASS, you
   can just delete the directory and use regular CSS without problems.

   (http://sass-lang.com, http://compass-style.org, https://github.com/twbs/bootstrap-sass)

* Out of the box setup of jQuery and modernizr AND important polyfills,
   that provide fallback solutions for CSS3 selectors, styling, media queries,
   and html5 tags. (Namely: selectivizr, respond, pie and html5shiv)

* (Frontend) package management with Bower and django-bower.
   (http://bower.io, https://github.com/nvbn/django-bower)

   The packages are specified in settings.py by BOWER_INSTALLED_APPS and
   downloaded/updated with ./manage.py bower_install

* CSS and JS management with compression and merging by django-pipeline.
   (https://django-pipeline.readthedocs.org/‎)

* A good base.html template

* A sane way to manage settings:
   There is a base settings.py file, all locally relevant settings are
   configured with ENVIRONMENT variables.

   For easy development, you can just do export ENV=dev to get preconfigured
   development settings.

   To check all available env variables, check settings.py comments in the
   first few lines, which provide a list.

* Stubs for custom management commands (./manage.py commands) and
   templatetag libraries that you can just copy and paste.

* A custom public/ directory that contains static and media directories and is
   the only one that's accessible publicly.

* A good seperation of requirements, with a requirements.txt file and
   custom files for the different environments.

* Sample configuration files for other applications, like an Apache2 virtual
   host.


License:
--------

Django-kickstart is under the BSD (3-clause) license.
See LICENSE.txt


Authors:
--------

Suggestions and contributions are very welcome!

* Christoph Herzog - http://theduke.at - chris@theduke.at


Behind the scenes:
------------------

The tool goes through these steps to set up the new project.

1. Start the new project.

> django-admin.py startproject --template="https://github.com/theduke/django-kickstart/archive/master.zip" --extension="py,gitignore,txt,md,conf" PROJECTNAME

2. Create virtualenv.

> cd PROJECT

Remove stub pyenv file:
> rm -r pyenv

Create virtualenv with name pyenv:
> virtualenv pyenv

Activate the new virtualenv:
> . pyenv/bin/activate

3. Install requirements.

> pip install -r app/requirements/development.txt

4. Several settings are configured with environment variables.
   To make it straight-forward for development, things are preconfigured
   for the dev environment. To activate it, just run:

   > export ENV=dev


5. Create sqlite database for development.

> app/manage.py syncdb
> app/manage.py migrate

6. Fetch bower packages.

app/manage.py bower_install

7. Set up a git repo

> git init
> git add .
> git commit -m "Initial commit"

7. Start building your awesome site.


Updating bootstrap-sass
-----------------------

After updating the bootstrap-sass GEM, you need to copy the
javascript and font assets!

cd to root (dir with this readme file in it)
cp -r $(bundle show bootstrap-sass)/vendor/assets/fonts/* app/apps/{{ project_name }}/static/fonts/
cp -r $(bundle show bootstrap-sass)/vendor/assets/javascripts/* app/apps/{{ project_name }}/static/js/
