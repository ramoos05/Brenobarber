# Breno Barber — Django

Site institucional + painel de agendamentos da Breno Barber.

---

## Requisitos

- Python 3.10+
- pip

---

## Instalação (desenvolvimento)

```bash
# 1. Clone o projeto e entre na pasta
cd brenobarber

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
# .venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o .env
cp .env.example .env
# Edite o .env e gere uma SECRET_KEY:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 5. Rode as migrations
python manage.py migrate

# 6. Crie o superusuário (para acessar o admin)
python manage.py createsuperuser

# 7. Suba o servidor
python manage.py runserver
```

Acesse:
- Site: http://localhost:8000
- Admin: http://localhost:8000/admin

---

## Estrutura do projeto

```
brenobarber/
├── brenobarber/
│   ├── settings/
│   │   └── base.py      ← configurações do projeto
│   ├── urls.py
│   └── wsgi.py
├── barbearia/            ← app principal
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py          ← validação do agendamento
│   ├── admin.py          ← painel Unfold com dashboard
│   └── urls.py
├── .env
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## Banco de dados

**Desenvolvimento:** SQLite (padrão, sem configuração extra)

**Produção:** PostgreSQL

```bash
# No .env de produção:
DATABASE_URL=postgres://usuario:senha@host:5432/brenobarber
```

Provedores gratuitos recomendados: Railway.app, Supabase, Render.com

---

## Deploy em produção

1. Preencha o `.env` com `DEBUG=False`, `SECRET_KEY` real e `DATABASE_URL`
2. Rode `python manage.py collectstatic`
3. Configure o servidor web (gunicorn + nginx, ou Railway/Render)

---

## Dashboard Admin (Unfold)

O painel `/admin` exibe:
- KPIs: agendamentos de hoje, confirmados e cancelados no mês
- Dashboard com gráfico dos últimos 30 dias
- Status colorido nos agendamentos (verde/vermelho)
- Filtro por data e busca por nome/telefone
# Brenobarber
