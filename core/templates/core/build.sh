#!/usr/bin/env bash
# Exit on error
set -o errexit

# Instala as dependências
pip install -r requirements.txt

# Coleta os arquivos estáticos (CSS, imagens do robô, etc.)
python manage.py collectstatic --no-input

# Prepara o banco de dados
python manage.py migrate

# Cria o superusuário automaticamente se ele não existir
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user, created = User.objects.get_or_create(username='matheusalmeida', defaults={'email': 'admin@example.com'}); user.set_password('200303'); user.is_superuser = True; user.is_staff = True; user.save()"
