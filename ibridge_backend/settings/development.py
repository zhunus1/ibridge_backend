from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': 'postgres',
        'PASSWORD': 'Behappy7+',
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}