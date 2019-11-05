from backend.settings.base import *
import os, json

DEBUG = True
ALLOWED_HOSTS = []

secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.get("DJANGO_SECRET")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': secrets.get("MYSQL_DB_NAME"),
        'USER': secrets.get("MYSQL_USER"),
        'PASSWORD': secrets.get("MYSQL_SECRET"),
        'HOST': secrets.get("MYSQL_HOST"),
        'PORT': secrets.get("MYSQL_PORT"),
    }
}