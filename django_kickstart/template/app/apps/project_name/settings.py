"""
Django settings for {{ project_name }}.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/


List of environment variables available:

ENV - the active environment

DEBUG - 1 or 0
TEMPLATE_DEBUG - 1 or 0

PUBLIC_DIR - the directory that holds publicly accessible files,
             expected subdirs are "media" and "static"
             if you want another setup, manually alter MEDIA_ROOT and STATIC_ROOT
VIRTENV_DIR - the root directory of the virtual env used

SECRET_KEY - the secret key
DB_ENGINE - the DB engine for the default DB
DB_NAME - the DB name for the default DB

ADMINS - the site admins, specify like this: ADMINS="admin1,admin 1@domain.com;admin 2,admin2@domain.com"
                          (seperate admins with ; and name from email with ,)

INTERNAL_IPS - separate by SPACE, like: INTERNAL_IPS="127.0.0.1 123.123.123.123"

EMAIL_BACKEND
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_USE_TLS

"""

import os

PROJECT_NAME = "{{ project_name }}"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# The virtual environment path. This is used in wsgi.py to put the virtual env
# on the PYTHONPATH automatically.
VIRTENV_DIR = os.environ.get('VIRTENV_DIR', os.path.join(ROOT_DIR, 'pyenv'))
# The path to the site packages used by the virtualenv.
# Note that this is relative to VIRTENV_DIR,
# so it might be "lib/python2.7/site-packages".
VIRTENV_PACKAGE_DIR = "__VIRTENV_PACKAGE_DIR__"

BASE_DIR = os.path.join(ROOT_DIR, 'app')
DATA_DIR = os.path.join(BASE_DIR, 'data')
PUBLIC_DIR = os.environ.get('PUBLIC_DIR', os.path.join(BASE_DIR, 'public'))

ENV = os.environ.get('ENV', 'production')

####################
# CORE             #
####################

DEBUG = bool(os.environ.get('DEBUG', True if ENV == 'dev' else False))
TEMPLATE_DEBUG = bool(os.environ.get('TEMPLATE_DEBUG', True if ENV == 'dev' else False))

# People who get code error notifications.
# In the format (('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com'))
# To specify with environment var, set it like this:
# ADMINS="admin1,admin1@domain.com;admin2,admin2@domain.com"
ADMINS = [l.split(',') for l in os.environ.get('ADMINS', '').split(';')]

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '127.0.0.1').split(' ')

# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
# For dev environment, this is set to all hosts.
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ')

# Local time zone for this installation. All choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name (although not all
# systems may support all possibilities). When USE_TZ is True, this is
# interpreted as the default user time zone.
TIME_ZONE = 'Europe/Vienna'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-DE'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to True, Django will format dates, numbers and calendars
# according to user current locale.
USE_L10N = False

# Not-necessarily-technical managers of the site. They get broken link
# notifications and other various emails.
MANAGERS = ADMINS

# Email address that error messages come from.
#SERVER_EMAIL = 'admin@DOMAIN.com'

# Database connection info. If left empty, will default to the dummy backend.
DATABASES = {}

# The email backend to use. For possible shortcuts see django.core.mail.
# The default is to use the SMTP backend.
# Third-party backends can be specified by providing a Python path
# to a module that defines an EmailBackend class.
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

# Host for sending email.
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')

# Port for sending email.
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 25))

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS', False))

# List of strings representing installed apps.

INSTALLED_APPS = (

    # CUSTOM apps.

    '{{ project_name }}',

    # CONTRIB apps.

    # Asset manager
    'pipeline',

    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Schema migration.
    'south',

    # Helpful debug toolbar.
    'debug_toolbar',

    # Form helpers.
    'crispy_forms',

    # Django bower integration.
    # https://github.com/nvbn/django-bower
    'djangobower',

    # DJANGO CORE apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Site framework, needed for allauth.
    'django.contrib.sites',

)

# List of locations of the template source files, in search order.
TEMPLATE_DIRS = ()

# List of callables that know how to import templates from various sources.
# See the comments in django/core/template/loader.py for interface
# documentation.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    # Allauth specific.
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

# Output to use in template system for invalid (e.g. misspelled) variables.
TEMPLATE_STRING_IF_INVALID = ''

# Default email address to use for various automated correspondence from
# the site managers.
#DEFAULT_FROM_EMAIL = 'no-reply@DOMAIN.com'

# Whether to append trailing slashes to URLs.
APPEND_SLASH = False

# Whether to prepend the "www." subdomain to URLs that don't have it.
PREPEND_WWW = False

# List of compiled regular expression objects representing URLs that need not
# be reported by BrokenLinkEmailsMiddleware. Here are a few examples:
#    import re
#    IGNORABLE_404_URLS = (
#        re.compile(r'^/apple-touch-icon.*\.png$'),
#        re.compile(r'^/favicon.ico$),
#        re.compile(r'^/robots.txt$),
#        re.compile(r'^/phpmyadmin/),
#        re.compile(r'\.(cgi|php|pl)$'),
#    )
IGNORABLE_404_URLS = ()

# SET IN local.py!!!
#
# A secret key for this particular Django installation. Used in secret-key
# hashing algorithms. See below in section "Environment specific".
#SECRET_KEY = ''

# Default module to use for urls.
ROOT_URLCONF = '{{ project_name }}.urls'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# The Python dotted path to the WSGI application that Django's internal servers
# (runserver, runfcgi) will use. If `None`, the return value of
# 'django.core.wsgi.get_wsgi_application' is used, thus preserving the same
# behavior as previous versions of Django. Otherwise this should point to an
# actual WSGI application object.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

##############
# MIDDLEWARE #
##############

# List of middleware classes to use.  Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.http.ConditionalGetMiddleware',
#     'django.middleware.gzip.GZipMiddleware',
)

##################
# AUTHENTICATION #
##################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

# The number of days a password reset link is valid for
PASSWORD_RESET_TIMEOUT_DAYS = 3

############
# FIXTURES #
############

# The list of directories to search for fixtures
FIXTURE_DIRS = (
    os.path.join(DATA_DIR, 'fixtures'),
)

###############
# STATICFILES #
###############

# A list of locations of additional static files
STATICFILES_DIRS = (
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

###########
# Logging #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file_requests': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(DATA_DIR, 'logs', 'requests.log'),
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(DATA_DIR, 'logs', 'security.log')
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file_requests'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


################
# APP SPECIFIC #
################

# Django Site framework settings.
SITE_ID = 1

# Crispy form helper settings.
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Bower settings.
BOWER_COMPONENTS_ROOT = DATA_DIR
BOWER_INSTALLED_APPS = (
    'jquery',
    'modernizr',

    # POLYFILLS: javascript fallback solutions for older browsers.

    # CSS3 selectors for IE 6-8.
    'selectivizr',
    # min/max width media queries for IE 6-8.
    'respond',
    # CSS3 styles for IE 6-8.
    'bower-pie',
    # HTML5 tag support for IE 6-8.
    'html5shiv',
)

# pipeline asset manager.

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_CSS = {
    'screen': {
        'source_filenames': (
            'css/screen.css',
        ),
        'output_filename': 'css/base.css',
        'extra_content': (),
    },
    'ie': {
        'source_filenames': (
            'css/ie.css',
        ),
        'output_filename': 'css/ie.css',
        'extra_content': (),
    },
    'print': {
        'source_filenames': (
            'css/print.css',
        ),
        'output_filename': 'css/print.css',
        'extra_content': (),
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
            'modernizr/modernizr.js',
            'jquery/dist/jquery.js',
            'js/bootstrap.js',
            'js/base.js',
        ),
        'output_filename': 'js/base.js',
    },
    'iepolyfills': {
        'source_filenames': (
            'html5shiv/dist/html5shiv.js ',
            'respond/dest/respond.src.js',
            'selectivizr/selectivizr.js',
        ),
        'output_filename': 'js/ie_poly.js'
    }
}


########################
# ENVIRONMENT SPECIFIC #
########################

# Many environment settings, like the database URL and the SECRET_KEY should
# be set with environment variables, and not in the code.
# Some things, like added enabled applications can be configured here though.
# The environment will be set by the ENV environment variable, and defaults
# to production.

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES['default'] = {
    'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
    'NAME': os.environ.get('DB_NAME')
}

# Default settings for development, so you can get started with coding right
# away.
if ENV == 'dev':
    # Set default sqlite database for development.
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db', 'db.sqlite3'),
    }

    # Default secret_key for dev.
    SECRET_KEY = '{{ secret_key }}'

    # To extend any settings from settings/base.py here's an example:
    INSTALLED_APPS = INSTALLED_APPS + ()

    DEBUG = TEMPLATE_DEBUG = True
    TEMPLATE_STRING_IF_INVALID = '<VAR_NONEXISTANT>'

    ALLOWED_HOSTS = ['*']

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(DATA_DIR, 'logs', 'debug.log'),
            },
            'console':{
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }
