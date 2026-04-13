# Breno Barber

Aplicação Django para o site da barbearia e o painel administrativo de agendamentos.

O projeto reúne:
- página institucional com formulário de agendamento
- regras de tarifa por dia para `Corte social`
- controle de horários disponíveis
- dashboard administrativo com métricas e gráficos no `/admin`

## Stack

- Python 3.10+
- Django 5
- django-unfold para o admin
- SQLite em desenvolvimento
- PostgreSQL em produção

# 🚀 Como rodar o projeto

```bash
git clone https://github.com/ramoos05/Brenobarber.git
cd Brenobarber
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver

URLs úteis:
- Site: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Configuração

As variáveis ficam no arquivo `.env`.

Campos mínimos para desenvolvimento:

```env
SECRET_KEY=sua-chave
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=
```

Se `DATABASE_URL` estiver vazio, o projeto usa SQLite.

## Estrutura principal

```text
brenobarber/
├── barbearia/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   └── templates/
├── brenobarber/
│   ├── settings/
│   │   └── base.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── manage.py
└── requirements.txt
```

## Regras de negócio atuais

- agendamentos novos são salvos como `confirmado`
- o formulário impede reservar um horário já ocupado
- a tarifa muda conforme o dia da semana para `Corte social`
- o valor salvo no agendamento é usado no dashboard para consolidar receita

## Qualidade

Comandos úteis:

```bash
python manage.py check
python manage.py test
```

Atualmente o projeto possui testes cobrindo:
- criação de agendamento
- bloqueio de horário já reservado
- aplicação automática da tarifa por dia
- carregamento básico da home

## Deploy

Antes de publicar:

```bash
python manage.py migrate
python manage.py collectstatic
```

Para produção, ajuste no `.env`:

```env
DEBUG=False
SECRET_KEY=sua-chave-real
DATABASE_URL=postgres://usuario:senha@host:5432/brenobarber
```
