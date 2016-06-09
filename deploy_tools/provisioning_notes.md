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
  sudo apt-get install apache2 postgersql postgersql-contrib libapache2-mod-wsgi git python3 python-pip python-dev python3-dev
  sudo pip install virtualenv virtualenvwrapper psycopg2

## Virtualenv wrapper config
  Add following lines to your .bashrc
  export WORKON_HOME=$HOME/~/Envs
  source /usr/local/bin/virtualenvwrapper.sh

## Apache Virtualhost config

* see httpd.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart Job

* restart apache2

## Folder Structure
Assume we have a user account at /home/username
