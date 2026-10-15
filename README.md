# BrenoBarber

Sistema web de agendamentos para barbearia, com área do cliente e painel admin. Desenvolvido em Django para uma barbearia real, atualmente em fase de testes.

## Tecnologias

<<<<<<< HEAD
Python, Django, SQLite, HTML e CSS.

## Como rodar
=======
Python, Django, PostgreSQL, HTML e CSS.

## Como rodar

Precisa do Python e de um PostgreSQL instalado. Crie um banco chamado `brenodb` e depois:
>>>>>>> e8a0eda (...)

git clone https://github.com/ramoos05/Brenobarber.git
cd Brenobarber

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

Abra o arquivo `.env` e preencha `SECRET_KEY` e `DB_PASSWORD` (a senha do seu Postgres). Depois:

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

O site abre em http://127.0.0.1:8000/ e o painel admin em http://127.0.0.1:8000/admin/ com o usuário que você criou no createsuperuser.

## Visão do usuário

 https://github.com/user-attachments/assets/214d4981-8a9d-4b9c-ab7a-24b37fc45177

## Visão do admin

https://github.com/user-attachments/assets/c365d5b3-d05a-449a-b8bf-b5b7da057fa5

<<<<<<< HEAD
## Status

Em desenvolvimento. Ainda não está publicado. Usa SQLite por padrão e está preparado para deploy (ex.: Render). A migração para PostgreSQL está nos próximos passos.

## Autor

=======
## Deploy

O projeto está pronto para publicar no Render, com o banco PostgreSQL no Neon:

1. No Neon, crie um projeto e copie a connection string.
2. No Render, crie um Blueprint apontando para este repositório (ele lê o `render.yaml`).
3. Quando o Render pedir, cole a connection string em `DATABASE_URL` e defina o e-mail e a senha do admin.
4. Em produção o Django usa `brenobarber.settings.prod`, que lê o banco da variável `DATABASE_URL`.

## Status

Em desenvolvimento e em fase de testes com a barbearia.

## Autor

>>>>>>> e8a0eda (...)
Patrick Ramos
