# ! python
# coding: utf-8
#--------------------------------
# all magic in the __init__.py
#--------------------------------


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os
import pytz


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')

SITE_ID=1


DEBUG = True
LOCAL_DEV = False
SECRET_KEY = ''

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
TZ = pytz.timezone(TIME_ZONE)
DATE_FORMAT = 'Y-m-d'
USE_I18N = True
USE_L10N = False
USE_TZ = True

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'wsgi.application'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'public', 'media')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'public', 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'compressor.finders.CompressorFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
#        'DIRS': [
#            os.path.join(BASE_DIR, 'templates/'),
#        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': False,
        }
    },
]

MIDDLEWARE_CLASSES = (
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
#    'django.contrib.sites', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django.contrib.flatpages',
    'django.contrib.admin',

#    "compressor",
    'apps.app',
)

EMAIL_SUBJECT_PREFIX = '[SITE] '

INTERNAL_IPS = ('127.0.0.1',)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

UPLOAD_FILES_DIR = os.path.join(MEDIA_ROOT, 'upload', 'files')

FILE_UPLOAD_PERMISSIONS = 0o644

