from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = "https://github.com/naveenpanwar/tgoat.git"

def deploy():
    site_folder = '/home/%s/superlists'%(env.user,)
    source_folder = site_folder+'/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, 'tgoat.com')
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)

def _create_directory_structure_if_necessary(site_folder):
    run('mkdir -p %s' % (site_folder,) )
    for subfolder in ('static','source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder) )

def _get_latest_source(source_folder):
    if exists(source_folder+'/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))

def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/superlists/settings.py'
    wsgi_path = source_folder + '/superlists/wsgi.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path, 'DOMAIN = "localhost"', 'DOMAIN = "%s"' % ( site_name,))
    sed(wsgi_path,
            'site.addsitedir("/home/naveen/Envs/tgoat/lib/python3.5/site-packages")',
            'site.addsitedir("/home/%s/Envs/tgoat/lib/python3.5/site-packages")' % (env.user,),
            )
    secret_key_file = source_folder + '/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = "~/Envs/tgoat"
    if not exists(virtualenv_folder+'/bin/pip'):
        run('mkvirtualenv -p python3 tgoat')
        run('%s/bin/pip install -r %s/requirements.txt'%(virtualenv_folder, source_folder))

def _update_static_files(source_folder):
    run( 'cd %s && ~/Envs/tgoat/bin/python3 manage.py collectstatic --noinput'%(source_folder) )

def _update_database(source_folder):
    run( 'cd %s && ~/Envs/tgoat/bin/python3 manage.py migrate --noinput'%(source_folder) )

