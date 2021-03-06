"""
Django settings for iotBV3 project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import sys

# Hack for running app directly.
sys.path.insert(0, os.path.abspath('..'))
# Hack for tests.
sys.path.insert(0, os.path.abspath('.'))

import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rvpiy+4fv(^+*oqw@)1%t^td#eni#av^t(x!x9$7)2#zn_ezw0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_HOST = 'teamheightline@mail.ru'
EMAIL_HOST_USER = '***'
EMAIL_HOST_PASSWORD = '***'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

ALLOWED_HOSTS = ["127.0.0.1", 'iot-backend-v3.herokuapp.com']
# ALLOWED_HOSTS = []
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# SECURE_SSL_REDIRECT = True
WHITENOISE_USE_FINDERS = True
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

ADMINS = (
    ('Heightline', 'teamheightline@mail.ru'),
)
# Application definition
# CORS_ALLOWED_ORIGINS = [
#     "https://iot-frontend-show-version.herokuapp.com/",
#     "http://localhost:3000/",
#     "http://127.0.0.1:3000/",
#     "*"
#
# ]
# CORS Config
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

INSTALLED_APPS = [
    'graphene_django',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',
    'usertests',

    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    "graphql_auth",
    'django_filters'
]


MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',

]

ROOT_URLCONF = 'iotBV3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iotBV3.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dd17od3d3n92nd',
        'USER': 'htlhhxjvfwaitz',
        'PASSWORD': '8b4a95477a04160af4e32e42a16eef0a300f16a4f2db715a9404d5675c89e28f',
        'HOST': 'ec2-54-159-175-113.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/




GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

GRAPHENE = {
    # 'iotBV3.schema.schema'
    'SCHEMA': 'iotBV3.schema.schema',
    'MIDDLEWARE': ['graphql_jwt.middleware.JSONWebTokenMiddleware'],
}

AUTHENTICATION_BACKENDS = [
    # 'graphql_jwt.backends.JSONWebTokenBackend',
    "graphql_auth.backends.GraphQLAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = 'users.CustomUser'
#
# import socket
# socket.getaddrinfo('127.0.0.1', 8080)
#
# import os
# assert 'SYSTEMROOT' in os.environ


# Activate Django-Heroku.
django_heroku.settings(locals())
