Provisioning a new site
=================================

## Required Packages:

* Apache
* mod_wsgi
* postgresql
* Python3
* python-dev
* python3-dev
* Git
* pip
* virtualenv
* virtualenv-wrapper
* psycopg2

e.g.,, on Ubuntu:
  sudo apt-get install apache2 postgersql postgersql-contrib git python3 python-pip python-dev python3-dev
  sudo pip install virtualenv virtualenvwrapper psycopg2 mod_wsgi

## Virtualenv wrapper config
  Add following lines to your .bashrc
  export WORKON_HOME=$HOME/Envs
  source /usr/local/bin/virtualenvwrapper.sh

## Apache Virtualhost config for embedded use of mod_wsgi

* see httpd.conf
* replace SITENAME with, e.g., staging.my-domain.com

## config for embedded use of mod_wsgi or using mod_wsgi as python-package

* python manage.py runmodwsgi --setup-only --port=80 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
* Create a systemd file to start this service on startup ex. apache_mod_wsgi.service with this content
* 
  [Unit]
  Description=apache2 with mod_wsgi

  [Service]
  Type=oneshot
  RemainAfterExit=yes
  ExecStart=/etc/mod_wsgi-express-80/apachectl start
  ExecStop=/etc/mod_wsgi-express-80/apachectl stop

  [Install]
  WantedBy=multi-user.target
  
* place it in /lib/systemd/system/
* restart the server

## Upstart Job

* restart apache2

## Folder Structure
Assume we have a user account at /home/username
