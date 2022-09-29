#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Ngnix HTTP'
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "This is a test for nginx configuration" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -fR ubuntu:ubuntu /data/
sed -i "28 a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
