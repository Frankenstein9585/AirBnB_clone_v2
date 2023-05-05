#!/usr/bin/env bash
# This scripts is used to setup web servers
if ! command -v nginx &> /dev/null
then
	sudo apt-get update -y
	sudo apt-get install nginx -y
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

cat > /data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

if [ -L /data/web_static/current ];
then
	sudo rm -r /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config="
server{
	listen 80 default_server;
        listen [::]:80 default_server;
	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}
}"

echo "$config" > /etc/nginx/sites-available/default
sudo service nginx restart
