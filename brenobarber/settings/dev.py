from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'brenodb',
        'USER': 'postgres',
        'PASSWORD': 'pp123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

