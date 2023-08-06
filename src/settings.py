import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-*$cr-g)l+2lan-mlvnzge#zyzpl8ocnmuobi-^=_y#483_g42='
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',  # Third party
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",  # Third Party 
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Third party 
    'modeltranslation', # Third party 
    'django.contrib.admin',

    # Local
    'app',

    # Third party
    'django_cleanup.apps.CleanupConfig',
    'rest_framework', 
    'corsheaders', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Third Party 
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Third Party 
    "corsheaders.middleware.CorsMiddleware",  # Third Party 
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Translation
LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')

# Third party 
REST_FRAMEWORK = { 
    "DEFAULT_PERMISSION_CLASSES": [ 
        "rest_framework.permissions.AllowAny", 
    ]
} 

# Third party
CORS_ALLOWED_ORIGINS = (
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5500",

    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
)
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5500",

    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
]
CORS_ORIGIN_ALLOW_ALL = True 

ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_L10N = True
USE_I18N = True
USE_TZ = True

LANGUAGES = (
    ('uz', 'Uzbek'),
    ('ru', 'Russia'),
    ('en', 'English'),
)

STATIC_URL = "/static/" 
STATIC_ROOT = BASE_DIR / "static" 
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" 
 
MEDIA_URL = '/media/' 
MEDIA_ROOT = BASE_DIR / 'media' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1 