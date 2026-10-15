from .base import *
import dj_database_url
from decouple import config

DEBUG = False

# Em produção a chave é obrigatória (sem valor padrão inseguro)
SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = [h.strip() for h in config("ALLOWED_HOSTS", default="").split(",") if h.strip()]

# O Render informa o domínio do serviço nesta variável
RENDER_HOST = config("RENDER_EXTERNAL_HOSTNAME", default="")
if RENDER_HOST:
    ALLOWED_HOSTS.append(RENDER_HOST)
    CSRF_TRUSTED_ORIGINS = [f"https://{RENDER_HOST}"]

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
        conn_max_age=600,
    )
}

# O Render termina o HTTPS antes do Django; sem isso o redirect para HTTPS entra em loop
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
