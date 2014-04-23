#!/bin/bash
 
NAME="hello_world"                                  # Name of the application
DJANGODIR=/vagrant/django/hello_world             # Django project directory
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=hello_world.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=hello_world.wsgi                     # WSGI module name

 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug \
  --bind=0.0.0.0:8000