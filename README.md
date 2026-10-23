# 💈 BrenoBarber

Sistema web de agendamentos para barbearia, desenvolvido com **Python e Django** para uma barbearia real.

A aplicação permite que clientes realizem agendamentos online e oferece um painel administrativo para gerenciamento de horários, serviços e atendimentos.

## 🛠️ Tecnologias

- **Backend:** Python e Django
- **Banco de dados:** PostgreSQL
- **Frontend:** HTML e CSS
- **Painel administrativo:** Django Admin / Unfold
- **Hospedagem:** Render
- **Banco de dados em nuvem:** Neon

## ✨ Funcionalidades

- Agendamento online de horários.
- Gerenciamento de serviços e agendamentos.
- Controle de horários disponíveis.
- Painel administrativo personalizado.
- Indicadores para acompanhamento dos atendimentos.
- Interface para clientes e administradores.

## 🎥 Demonstração

### Visão do cliente

https://github.com/user-attachments/assets/214d4981-8a9d-4b9c-ab7a-24b37fc45177

### Visão do administrador

https://github.com/user-attachments/assets/c365d5b3-d05a-449a-b8bf-b5b7da057fa5

## 🚀 Como executar localmente

**1. Clone o repositório**

```bash
git clone https://github.com/ramoos05/Brenobarber.git
cd Brenobarber
```

**2. Crie e ative o ambiente virtual (Windows)**

```powershell
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**

```powershell
pip install -r requirements.txt
```

**4. Configure o banco de dados**

Instale o PostgreSQL e crie um banco chamado `brenodb`.

Copie o arquivo de exemplo:

```powershell
copy .env.example .env
```

Configure no `.env` as variáveis necessárias, incluindo `SECRET_KEY` e `DB_PASSWORD`.

**5. Execute as migrações e inicie o servidor**

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

A aplicação estará disponível em:

- **Site:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

## ☁️ Deploy

O projeto possui configuração para implantação no **Render**, utilizando **PostgreSQL no Neon**.

1. Crie um projeto no Neon e obtenha a connection string.
2. No Render, crie um Blueprint conectado ao repositório.
3. Configure `DATABASE_URL` e as demais variáveis de ambiente necessárias.
4. Em produção, o Django utiliza `brenobarber.settings.prod`.

## 📌 Status

O BrenoBarber está em fase de testes com uma barbearia real, com foco em melhorias contínuas e evolução das funcionalidades.

## 👨‍💻 Desenvolvedor

**Patrick Ramos**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em Backend Python e desenvolvimento de aplicações web.

[GitHub](https://github.com/ramoos05) • [LinkedIn](https://www.linkedin.com/in/ramos-dev/)
