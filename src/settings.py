import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-*$cr-g)l+2lan-mlvnzge#zyzpl8ocnmuobi-^=_y#483_g42='
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',  #Third party
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",  # Third Party 
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Third party 

    # Local
    'app',

    # Third party
    'rest_framework', 
    'rest_framework.authtoken', 
    'corsheaders', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Third Party 
    "corsheaders.middleware.CorsMiddleware",  # Third Party 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Third party 
REST_FRAMEWORK = { 
    "DEFAULT_PERMISSION_CLASSES": [ 
        "rest_framework.permissions.AllowAny", 
    ], 
    "DEFAULT_AUTHENTICATION_CLASSES": [ 
        "rest_framework.authentication.SessionAuthentication", 
        "rest_framework.authentication.TokenAuthentication", 
    ], 
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", 
 
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', 
    # 'PAGE_SIZE': 3
} 

"""# Third party 
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
] """

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

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/" 
# STATICFILES_DIRS = [BASE_DIR / "static"] 
STATIC_ROOT = BASE_DIR / "static" 
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" 
 
MEDIA_URL = '/media/' 
MEDIA_ROOT = BASE_DIR / 'media' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1 