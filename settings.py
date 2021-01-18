"""
Laurent's note: for backup local settings.py in actweb django_local use

Django settings for actweb_0911 project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(a7)u3tbw+&c#dn1v6to2(pdzuq8qt-$=466pp@(9tr3!avpc%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','.pfcfatapi.top','.deeptrade.pfcf.com.tw']


# Application definition

INSTALLED_APPS = [
    'drf_multiple_model',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'mod_wsgi.server',
    'commodity_sort',
    'Kbar_regnization',
    'eco_running',
    'stockf',
    'trend_indicator',
    'commodity_quote',
    'cot_api',
    'pages',
    'img_upload',

]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'actweb_0911.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'actweb_0911.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'calculate',                       # Or path to database file if using sqlite3.
        'USER': 'webmysql@actwebdb2',                       # Not used with sqlite3.
        'PASSWORD': 'AIteam168',               # Not used with sqlite3.
        'HOST': '103.17.9.213',                           # Set to empty string for 103.17.9.213. Not used with sqlite3.
        'PORT':3306,                           # Set to empty string for default. Not used with sqlite3.
        #'OPTIONS': {
         #   'ssl': {'ssl-ca': '/var/www/html/BaltimoreCyberTrustRoot.crt.pem'}
        #}
    },
    'db2': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'webaiuse',  # Or path to database file if using sqlite3.
        'USER': 'webmysql@actwebdb2',  # Not used with sqlite3.
        'PASSWORD': 'AIteam168',  # Not used with sqlite3.
        'HOST': '103.17.9.213',  # Set to empty string for 103.17.9.213. Not used with sqlite3.
        'PORT': 3306,  # Set to empty string for default. Not used with sqlite3.
    },
    'webmarquee': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'webmarquee',  # Or path to database file if using sqlite3.
            'USER': 'webmysql@actwebdb2',  # Not used with sqlite3.
            'PASSWORD': 'AIteam168',  # Not used with sqlite3.
            'HOST': '103.17.9.213',  # Set to empty string for 103.17.9.213. Not used with sqlite3.
            'PORT': 3306,  # Set to empty string for default. Not used with sqlite3.
    },
    'stockfuture': {
                'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'stockfuturedata_day',  # Or path to database file if using sqlite3.
                'USER': 'webmysql@actwebdb2',  # Not used with sqlite3.
                'PASSWORD': 'AIteam168',  # Not used with sqlite3.
                'HOST': '103.17.9.213',  # Set to empty string for 103.17.9.213. Not used with sqlite3.
                'PORT': 3306,  # Set to empty string for default. Not used with sqlite3.
    },
    'pricedata': {
                'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'pricedata_day',  # Or path to database file if using sqlite3.
                'USER': 'webmysql@actwebdb2',  # Not used with sqlite3.
                'PASSWORD': 'AIteam168',  # Not used with sqlite3.
                'HOST': '103.17.9.213',  # Set to empty string for 103.17.9.213. Not used with sqlite3.
                'PORT': 3306,  # Set to empty string for default. Not used with sqlite3.
        },
    'cotdatabase': {
                'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'cotdatabase',  # Or path to database file if using sqlite3.
                'USER': 'webmysql@actwebdb2',  # Not used with sqlite3.
                'PASSWORD': 'AIteam168',  # Not used with sqlite3.
                'HOST': '103.17.9.213',  # Set to empty string for 103.17.9.213. Not used with sqlite3.
                'PORT': 3306,  # Set to empty string for default. Not used with sqlite3.
        },
    'imgsave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'imgdatabase',
        'USER': 'webmysql@actwebdb2',
        'PASSWORD': 'AIteam168',
        'HOST': '103.17.9.213',
        'PORT': 3306
    }
}

DATABASE_ROUTERS = ['actweb_0911.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    'commodity_sort': 'default',
    'Kbar_regnization': 'db2',
    'eco_running': 'webmarquee',
    'stockf': 'stockfuture',
    'trend_indicator':'default',
    'commodity_quote':'pricedata',
    'cot_api':'cotdatabase',
    'img_upload':'imgsave',
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "templates/static"),
)
STATIC_ROOT = (
    os.path.join(BASE_DIR, "templates/static_root")
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'templates/media').replace('\\', '/')
MEDIA_URL = '/media/'