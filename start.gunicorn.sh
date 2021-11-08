#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

#python manage.py compilemessages
python manage.py migrate
python manage.py collectstatic --noinput

echo "
from django.contrib.auth.models import User;
if not User.objects.filter(username='${DJANGO_SUPERUSER_USER}').exists():
    User.objects.create_superuser(
        '${DJANGO_SUPERUSER_USER}',
        '${DJANGO_SUPERUSER_EMAIL}',
        '${DJANGO_SUPERUSER_PASSWORD}'
    )
" | python manage.py shell || /bin/true

gunicorn --bind 0.0.0.0:8000 ibridge_backend.wsgi -w $WORKERS
