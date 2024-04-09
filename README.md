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
