#
# coding: utf-8
# ======================
# Reads settings variables from environment
#
#


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from .base import *


def set_global_var_from_dict(dict_, prefix='', json_prefix='JSON_'):

    def dict_get(name, default=None):
        return dict_.get("%s%s" % (prefix, name), default)

    def dict_get_json(name, default=None):
        return dict_.get("%s%s%s" % (prefix, json_prefix, name), default)

    def second(name):
        val = globals().get(name)
        val = dict_get(name, val)
        maybe_json = dict_get_json(name)
        if maybe_json:
            val = json.loads(maybe_json)
        globals()[name] = val

    return second


#
# VARNAMEs which may be loaded from env if exists in env
# PREFIX_VARNAME - it is a string variable
# PREFIX_JSON_VARNAME - it is a json encoded variable
#
# For exaple put in your env: DJANGO_JSON_DEBUG=true
env_vars = [
    'DATABASES',
    'ALLOWED_HOSTS',
    'SECRET_KEY',
    'DEBUG',
    'MEDIA_ROOT',
    'STATIC_ROOT',
    'COMPRESS_ENABLED',
    'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY',
    'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET',
    'SOCIAL_AUTH_FACEBOOK_KEY',
    'SOCIAL_AUTH_FACEBOOK_SECRET',
    'SOCIAL_AUTH_TWITTER_KEY',
    'SOCIAL_AUTH_TWITTER_SECRET',
    'TEMPLATE_DEBUG',
]


for name in env_vars:
    set_global_var_from_dict(os.environ, 'DJANGO_')(name)


TEMPLATES[0]['OPTIONS']['debug'] = globals().get('TEMPLATE_DEBUG', False)
