# Django Subway
Based on Django-Starter-Kit by Grigoriy Bezyuk <greg@everlearning.me>

## Development Setup
```
# TODO: check if virtualenv really works this way
./setup-dev.sh
. venv/bin/activate
```

## Production Setup
```
# TODO: more detailed description
./setup-dev.sh
./manage.py collectstatic
. venv/bin/activate
pip install gunicorn
# create system user to run as
# configure database
# see examples bellow
```

### Gunicorn Unix-socket setup example
```
#!/bin/bash
NAME="django_subway"
DJANGODIR=/webapps/django_subway/
SOCKFILE=/webapps/django_subway/run/gunicorn.sock
USER=django_subway_user
GROUP=webapps
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=core.settings
DJANGO_WSGI_MODULE=core.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
. /webapps/django_subway/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE
```

### Supervisord configuration example
```
[program:django_subway_backend]
command = /webapps/django_subway/bin/gunicorn_start
user = django_subway_user
stdout_logfile = /webapps/django_subway/logs/gunicorn_supervisor.log
redirect_stderr = true
autostart=true
autorestart=unexpected
```

### Nginx Vhost example
```
upstream backend_django_subway {
  server unix:/webapps/django_subway/run/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name django_subway.gbezyuk.ru;

    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $host;

    client_max_body_size 4G;

    access_log /webapps/django_subway/logs/nginx-access.log;
    error_log /webapps/django_subway/logs/nginx-error.log;

    location /static/ {
        alias   /webapps/django_subway/static/;
    }
    location /media/ {
        alias   /webapps/django_subway/media/;
    }

    location / {
        if (!-f $request_filename) {
            proxy_pass http://backend_django_subway;
            break;
        }
    }
}
```
