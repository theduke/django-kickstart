import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-kickstart',
    version = '0.1',
    packages = ['django_kickstart'],
    include_package_data = True,
    scripts = ['bin/django-kickstart'],
    entry_points = {
        'console_scripts': [
            'django-kickstart = django_kickstart.cli:main'
        ]
    },
    install_requires = [
        'Django',
        'virtualenv',
    ],
    license = 'BSD License',
    description = 'Tool for kickstarting django projects.',
    long_description = README,
    url = 'https://github.com/theduke/django-kickstart',
    author = 'Christoph Herzog',
    author_email = 'chris@theduke.at',
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
