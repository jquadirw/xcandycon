"""
Django settings for xcandyapp project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '96dt2k*z!ulip__5rbvane8=!@5xxh1fs$7b8e2^s_)p%+pb7x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'xcandyapp.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp.apps.WebappConfig',
    'social_django',
    'crispy_forms',
    'widget_tweaks',
    'bootstrap_modal_forms',
    'whitenoise.runserver_nostatic'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'xcandyapp.urls'

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

WSGI_APPLICATION = 'xcandyapp.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# PostgreSQL (local)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'OPTIONS': {
#             'options': '-c search_path=xcandymin'
#         },
#         'NAME': 'xcandydb',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES['default'] =  dj_database_url.config()

# PostgreSQL (heroku)
# SECRET_KEY = config('SECRET_KEY')
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL')
#     )
# }

# MySQL settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'xcandydb',
#         'USER': 'xcandydb_owner',
#         'PASSWORD': 'abcd.1234',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Heroku MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'heroku_9887d068c78a589',
#         'USER': 'ba75e39f324d83',
#         'PASSWORD': '39d06b3f',
#         'HOST': 'us-cdbr-east-05.cleardb.net',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'xcandyapp/static'),
)

# print("static root = ", STATIC_ROOT)
# print("static url = ", STATIC_URL)

# Auth0 settings
SOCIAL_AUTH_TRAILING_SLASH = False  # Remove trailing slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-utjtfsx4.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = '8SY0HohBHyj0vMT0yHJ2j7gmjzACbL62'
SOCIAL_AUTH_AUTH0_SECRET = 'DKBIoM8QlFOhzRWnJXSeMOeUtad1pi8xYLnSp1tt7qpzB5pM2khsi0a7nnR_uf1w'
SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email'
]
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'webapp.authentication.authorization.process_roles',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = {
    'webapp.authentication.auth0.Auth0',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend'
}

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/'

# caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "rdai"
    }
}
CACHE_TTL = 60 * 15


# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

