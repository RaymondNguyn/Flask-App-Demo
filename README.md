Create virtual enviroment
`python3 -m venv ~/env/nginx`

Initalize it
`source ~/env/nginx/bin/activate`


flask.service file in `/etc/systemd/system`
```
[Unit]
Description=Gunicorn/Flask
After=network.target

[Service]
User=ray
WorkingDirectory=/home/ray/nginx-server
Environment="PATH=/home/ray/env/nginx/bin"
ExecStart=/home/ray/env/nginx/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 wsgi:app

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
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

}
```

```
/app.py
from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__)

@app.route("/api")
def home():
    return render_template("base.html")

@app.route("/api/test")
def test():
    return render_template("test.html")

@app.route("/api/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
```

```
/wsgi.py
from app import app

if __name__ == '__main__':
    app.run()
```
