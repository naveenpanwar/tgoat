Provisioning a new site
=================================

## Required Packages:

* Apache
* Python3
* Git
* pip
* virtualenv
* virtualenv-wrapper

e.g.,, on Ubuntu:
  sudo apt-get install apache2 libapache2-mod-wsgi git python3 python-pip
  sudo pip install virtualenv virtualenvwrapper

## Apache Virtualhost config

* see httpd.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart Job

* restart apache2

## Folder Structure
Assume we have a user account at /home/username
