# tgoat
Learning TDD with Follow The Testing Goat

# Provisioning notes

## Configuring Nginx

The configuration template below is the configuration for nginx
server and the first three lines helps when you want to serve 
two are more sites from the same server

place this file at `/etc/nginx/sites-available/sitename`

```conf
  upstream ventury_server {
    server unix:/tmp/ventury.socket fail_timeout=0;
  }

  server {
    listen 80;
    server_name ventury.com;
    
    location /static {
      alias /home/naveen/ventury/static;
    }
    
    location / {
      proxy_set_header Host $host;
      proxy_pass http://unix:/tmp/ventury.socket;
    }
  }
```
## Configuring gunicorn

To configure gunicorn to start at system start using `systemd`
create a file from template file below

place this file at `/etc/systemd/system/gunicorn-sitename.service`

```conf
  [Unit]
  Description=gunicorn daemon for superlists
  After=network.target

  [Service]
  User=naveen
  Group=naveen
  WorkingDirectory=/home/naveen/superlists/source
  ExecStart=/home/naveen/Envs/tgoat/bin/gunicorn --workers 3 --bind unix:/tmp/superlists.socket superlists.wsgi:application

  [Install]
  WantedBy=multi-user.target
```
after this

* sudo systemctl daemon-reload
* sudo systemctl enable gunicorn-sitename.service
* sudo systemctl start gunicorn-sitename.service
