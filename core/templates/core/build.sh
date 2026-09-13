#!/usr/bin/env bash
# Exit on error
set -o errexit

# Instala as dependências
pip install -r requirements.txt

# Coleta os arquivos estáticos (CSS, imagens do robô, etc.)
python manage.py collectstatic --no-input

# Prepara o banco de dados
python manage.py migrate
