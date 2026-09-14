#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Cria o superusuário de forma segura sem quebrar se ele já existir
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='matheusalmeida').exists() or User.objects.create_superuser('matheusalmeida', 'admin@example.com', '123456')"
