# 💈 BrenoBarber - Sistema de Barbearia

Sistema web para gerenciamento de barbearia, com foco em agendamentos e organização do dia a dia.

---

## 🚀 Rodar o projeto (rápido)

```bash
git clone https://github.com/ramoos05/Brenobarber.git
cd Brenobarber

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

python manage.py migrate
python manage.py runserver
```

---

## 🌐 Acesse no navegador

* 👤 Versão usuário:
  http://127.0.0.1:8000/

* 🔧 Painel admin:
  http://127.0.0.1:8000/admin/

---

## 🔑 Acesso de teste

> ⚠️ Apenas para ambiente de desenvolvimento

**Admin**

* Usuário: `breno`
* Senha: `breno123`

---

## 🧠 Observações

* Usa SQLite por padrão (não precisa configurar banco)
* Variáveis de ambiente ficam no arquivo `.env`
* Projeto preparado para deploy (ex: Render)

---

## 👨‍💻 Autor

Desenvolvido por **Patrick Ramos** 💈
