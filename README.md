# BrenoBarber

Sistema web de agendamentos para barbearia, com área do cliente e painel admin. Desenvolvido em Django para uma barbearia real, atualmente em fase de testes.

## Tecnologias

Python, Django, SQLite, HTML e CSS.

## Como rodar

git clone https://github.com/ramoos05/Brenobarber.git
cd Brenobarber

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

O site abre em http://127.0.0.1:8000/ e o painel admin em http://127.0.0.1:8000/admin/ com o usuário que você criou no createsuperuser.

## Visão do usuário

 https://github.com/user-attachments/assets/214d4981-8a9d-4b9c-ab7a-24b37fc45177

## Visão do admin

https://github.com/user-attachments/assets/c365d5b3-d05a-449a-b8bf-b5b7da057fa5

## Status

Em desenvolvimento. Ainda não está publicado. Usa SQLite por padrão e está preparado para deploy (ex.: Render). A migração para PostgreSQL está nos próximos passos.

## Autor

Patrick Ramos
