import sys
import os
import argparse
import re
import subprocess
import shutil

TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template')

def which(program):
    """
    Check path for an executable, or return None if not found.

    Taken from: http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    """
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def file_replace(path, patterns):
    """
    Replace one or more patterns in a file.
    """

    content = open(path).read()

    if type(patterns[0] == str):
        patterns = (patterns,)

    for pattern in patterns:
        content = content.replace(pattern[0], pattern[1])

    open(path, 'w').write(content)


class Cli(object):


    def run(self):
        parser = self.get_parser()
        args = parser.parse_args()

        if not self.check_requirements(args):
            sys.exit(1)

        if not self.check_args(args):
            sys.exit(1)

        print("Creating project " + args.name)
        self.create(args)


    def get_parser(self):
        parser = argparse.ArgumentParser(description='Kickstart a Django project.')
        parser.add_argument('--vcs', default='git', help="Set up a version control repository. Supported values: git|none")
        parser.add_argument('--virtualenv', help="Location for python virtualenv. If it already exists, the existing one will be used. Otherwise, a new one will be created.")
        parser.add_argument('--no-venv', action="store_true", help="Do not create a new virtual env, and not use an existing one. The system default will be used.")
        parser.add_argument('--no-db', action="store_true", help="Do not create a develoopment sqlite database.")
        parser.add_argument('--no-bower', action="store_true", help="Do not set up bower.")
        parser.add_argument('--verbose', '-v', action='store_true', help="More verbose output.")
        parser.add_argument('--domain', help="Domain that will be used in various parts of the setup.")
        parser.add_argument('--path', help="Parent directory for the new project. Defaults to current working dir.")
        parser.add_argument('--force', action="store_true", help="Delete old project if present.")
        parser.add_argument('name', help="Name of the new project.")

        return parser


    def check_args(self, args):
        name = re.sub(r'[^a-z0-9\_]', '', args.name).lower()
        if name != args.name:
            print("Invalid project name! Only use lower case letters, numbers or an underscore!")
            return False



        if args.path:
            path = os.path.realpath(args.path)
            if not os.path.exists(path):
                print("Given parent directory '{p}' does not exist, please create it first.".format(p=path))
                return False

        path = args.path if args.path else os.getcwd()
        path = os.path.join(path, name)

        if os.path.exists(path):
            if args.force:
                shutil.rmtree(path)
            else:
                print("Directory {d} already exists, delete it first or run with --force.".format(d=path))
                return False

        args.path = path

        return True

    def check_requirements(self, args):
        """
        Check the neccessary requirements for the installation.
        """

        print("Checking requirements...")

        # Check django-admin

        if not which('django-admin.py'):
            print("django-admin.py was not found on your path! Please ensure that Django is installed by running 'pip install Django'.")
            return False

        # Check virtualenv.
        if not args.no_venv:
            try:
                import virtualenv
            except:
                print("virtualenv was not found on your path! Please ensure that it is installed by running 'pip install virtualenv' OR disable virtualenv creation by specifying --no-venv.")
                return False

        # Check vcs.
        vcs = args.vcs

        if vcs not in ('', 'none'):
            if vcs == 'git':
                # Check that git is on path.
                if not which('git'):
                    print("Git was not found on your path. Disable git repo creation with '--vcs=none'.")
                    return False
            else:
                print("Unsupported options for --vcs: '{v}'".format(v=vcs))
                return False

        # Check for bower.
        if not args.no_bower:
            if not which('bower'):
                print("bower was not found on your path! Ensure that bower is installed (npm install -g bower).")
                return False

        return True


    def create_project(self, name):
        code = subprocess.call([
            'django-admin.py',
            'startproject',
            '--template=' + TEMPLATE_PATH,
            '--extension=py,gitignore,txt,md,conf',
            name
        ])
        if code != 0:
            print("Error: django-admin.py failed")
            sys.exit(1)


    def create_virtualenv(self, path, settings_path):
        os.remove(os.path.join(path, '.gitkeep'))
        os.rmdir(path)

        import virtualenv

        virtualenv.create_environment(path,
            site_packages=True,
            unzip_setuptools=True,
        )


    def update_sitepackage_settings(self, virtualenv_path, settings_path, args):

        if not args.no_venv:
            # We need to update the VIRTENV_PACKAGE_DIR setting in settings.py
            # since it is needed for manage.py and wsgi.py.

            # Obviously skipped when no virtenv is created or used.

            # Determine virtualenv site packages location.
            site_packages_dir = subprocess.check_output([
                os.path.join(virtualenv_path, 'bin', 'python'),
                '-c',
                'from distutils.sysconfig import get_python_lib; print(get_python_lib())'
            ])
            site_packages_dir = site_packages_dir.replace("\n", "").replace(virtualenv_path + '/', "")

            # Now update the VIRTENV_PACKAGE_DIR setting.
            file_replace(settings_path, ('__VIRTENV_PACKAGE_DIR__', site_packages_dir))


    def install_python_requirements(self, pip, requirements_file):
        code = subprocess.call([pip, 'install', '-r', requirements_file])
        if code != 0:
            print("Error: Installing requirements with pip failed!")
            sys.exit(1)


    def create_db(self, manage_path, env):
        code = subprocess.call([manage_path, 'syncdb', '--migrate', '--noinput'], env=env)
        if code != 0:
            print("Error: could not run manage.py syncdb!")
            sys.exit(1)


    def fetch_bower_packages(self, manage_path, env):
        code = subprocess.call([manage_path, 'bower_install'], env=env)
        if code != 0:
            print("Error: Could not run manage.py bower_install")
            sys.exit(1)


    def create_vcs_git(self, path):
        os.chdir(path)
        code1 = subprocess.call(['git', 'init'])
        code2 = subprocess.call(['git', 'add', '-A'])
        code3 = subprocess.call(['git', 'commit', '-m', 'Initial commit by django-kickstart.'])

        if code1 != 0 or code2 != 0 or code3 != 0:
            print("Git repo creation failed!")
            sys.exit(1)


    def create(self, args):
        # Define all the paths.
        venv = args.virtualenv if args.virtualenv else os.path.join(args.path, 'pyenv')
        pip_bin = os.path.join(venv, 'bin', 'pip')
        app_path = os.path.join(args.path, 'app')
        django_manage = os.path.join(app_path, 'manage.py')
        settings_path = os.path.join(app_path, 'apps', args.name, 'settings.py')
        req_file = os.path.join(app_path, 'requirements', 'development.txt')

        # Prepare new env for manage.py commands.
        env = os.environ.copy()
        env['ENV'] = 'dev'

        # First, start new project with django-admin.
        print("Creating new project with django-admin.py...")
        self.create_project(args.name)

        # Create virtualenv.
        if not args.no_venv:
            if os.path.isdir(venv) and not os.path.isfile(os.path.join(venv, '.gitkeep')):
                print("Using virtual env " + venv)
            else:
                print("Creating new custom virtualenv...")
                self.create_virtualenv(venv, settings_path)

        self.update_sitepackage_settings(venv, settings_path, args)

        # Installing requirements.
        print('Installing python dependencies into virtualenv...')
        self.install_python_requirements(pip_bin, req_file)

        # Create developoment database, unless skipped by options.
        if not args.no_db:
            print("Creating development sqlite database and running south migrations...")
            self.create_db(django_manage, env)

        # Fetch bower packages.
        if not args.no_bower:
            print("Fetching bower packages...")
            self.fetch_bower_packages(django_manage, env)

        # Create vcs repository.
        if args.vcs == 'git':
            print("Creating GIT repository and making initial commit...")
            self.create_vcs_git(args.path)

        print("-" * 80)
        print("All done! Your new project is ready to use.")


def main():
    cli = Cli()
    cli.run()

if __name__ == "__main__" :
    main()
