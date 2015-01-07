#!/usr/bin/env bash

#http://source.mihelac.org/2009/10/23/django-avoiding-typing-password-for-superuser/

rm syaweb.db -rf
python manage.py syncdb --all --noinput
# python manage.py createsuperuser --username=admin --email=admin@qjmy.cn
python manage.py migrate --fake
python manage.py syncdb --noinput
python manage.py migrate
python manage.py cms check
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@qjmy.cn', 'pass')" | python manage.py shell
python manage.py runserver 0.0.0.0:81
