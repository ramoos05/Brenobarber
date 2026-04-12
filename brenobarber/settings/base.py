from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config("SECRET_KEY")

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms", 

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "barbearia",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "brenobarber.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   
        "APP_DIRS": True,                   
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "brenobarber.wsgi.application"

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

UNFOLD = {
    "SITE_TITLE": "Breno Barber",
    "SITE_HEADER": "Breno Barber",
    "SITE_URL": "/",
    "SITE_SYMBOL": "content_cut",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "COLORS": {
        "primary": {
            "50":  "255 241 241",
            "100": "255 218 218",
            "200": "255 179 179",
            "300": "255 130 130",
            "400": "255 75  75",
            "500": "239 68  68",
            "600": "220 38  38",
            "700": "185 28  28",
            "800": "153 27  27",
            "900": "127 29  29",
            "950": "69  10  10",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Operação"),
                "separator": True,
                "items": [
                    {
                        "title": _("Agendamentos"),
                        "icon": "calendar_month",
                        "link": "/admin/barbearia/agendamento/",
                        
                    },
                    {
                        "title": _("Horários"),
                        "icon": "schedule",
                        "link": "/admin/barbearia/horario/",
                    },
                ],
            },
            {
                "title": _("Catálogo"),
                "separator": True,
                "items": [
                    {
                        "title": _("Serviços"),
                        "icon": "content_cut",
                        "link": "/admin/barbearia/servico/",
                    },
                    {
                        "title": _("Tarifas por Dia"),
                        "icon": "payments",
                        "link": "/admin/barbearia/tarifadia/",
                    },
                    {
                        "title": _("Planos"),
                        "icon": "card_membership",
                        "link": "/admin/barbearia/plano/",
                    },
                ],
            },
            {
                "title": _("Configuração"),
                "separator": True,
                "items": [
                    {
                        "title": _("Dados da Barbearia"),
                        "icon": "settings",
                        "link": "/admin/barbearia/configuracao/",
                    },
                ],
            },
        ],
    },
    
    "DASHBOARD_CALLBACK": "barbearia.admin.dashboard_callback",
    "DASHBOARD_TEMPLATE": "admin/index.html",  # ← adiciona isso
    "STYLES": [
        "/static/admin/custom.css",
    ],
}
