#!/bin/bash

python manage.py migrate

python manage.py collectstatic --no-input

uwsgi --module app.wsgi:application \
      --env DJANGO_SETTINGS_MODULE=app.settings \
      --master --pidfile=/tmp/project-master.pid \
      --socket=:49152 \
      --processes=5 \
      --uid=1001 --gid=1001 \
      --max-requests=5000 \
      --vacuum \
