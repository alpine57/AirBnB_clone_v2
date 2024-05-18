#!/usr/bin/env bash
# Sets up web server for deployment of web static

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
config="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
sudo echo "$config" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx reload
