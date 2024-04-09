Install python
`python3 -m venv ~/env/nginx`

Create virtual enviroment
`source ~/env/nginx/bin/activate`


flask.service file in `/etc/systemd/system`
```
[Unit]
Description=Gunicorn/Flask
After=network.target

[Service]
User=ray
WorkingDirectory=/home/ray/nginx-server
Enviroment="PATH=/home/ray/env/nginx/bin/gunicorn --workers 3 --bind:0.0.0.0:8000 wsgi:app"

[Install]
WantedBy=multi-user.target
```

NGINX Server file in `/etc/nginx/sites-enabled`
```
server {
    listen 80;
    listen [::]:80;
    server_name 164.92.75.138;
    root /web/html/nginx-2420;
    location / {
        index index.php index.html index.htm;
    }

    location /api {
        # Define the reverse proxy settings
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

}
```
