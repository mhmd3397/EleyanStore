# eleyan_store/settings.py
from django.utils.translation import gettext_lazy as _
import os
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

config = config()

DEBUG = True
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

SECRET_KEY = config('DJANGO_SECRET_KEY', default='your_secret_key')

# Language and timezone settings
LANGUAGES = [
    ('ar', _('Arabic')),
    ('en', _('English')),
    ('he', _('Hebrew')),
]

LANGUAGE_CODE = 'ar'
USE_TZ = True
USE_I18N = True
USE_L10N = True

# Installed apps
INSTALLED_APPS = [
    'products',
    'users',  # Add the 'users' app here
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add other apps as needed
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Add this line
]

# Template settings
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

# Add the following lines for static and media files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Internationalization
LOCALE_PATHS = [
    BASE_DIR / 'locale',  # Add this line
]

# Add the following lines for authentication
AUTH_USER_MODEL = 'users.UserProfile'
LOGIN_URL = 'user_login'
LOGIN_REDIRECT_URL = 'home'
