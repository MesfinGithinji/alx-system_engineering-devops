#!/usr/bin/env bash
# Bash script that prepares the web servers for web_static deployment
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    <h1>Welcome to Hbnb</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
