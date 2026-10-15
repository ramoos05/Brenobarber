#!/usr/bin/env bash
# Script de build usado pelo Render
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Cria o admin na primeira vez (o plano grátis do Render não tem terminal).
# Só roda se as variáveis DJANGO_SUPERUSER_* estiverem definidas.
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --no-input || true
fi
