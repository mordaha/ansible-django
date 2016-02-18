# !python
# coding: utf-8
# ==========================================
# Test settings, avoids migrations and uses md5 passwords hashes to speed up tests
#   and sqlite database
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from os import environ
from .base import *


class NoMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"


DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

MIGRATION_MODULES = NoMigrations()

SECRET_KEY = '123'

# for Teamcity CI
if environ.get('TEAMCITY_TESTS'):
    TEST_RUNNER = "teamcity.django.TeamcityDjangoRunner"
