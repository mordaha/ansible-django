#
# coding: utf-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .base import *
from .environment import *

APP_ENV = os.environ.get('APP_ENV', 'dev')

if APP_ENV == 'dev':
    from .dev import *

if APP_ENV == 'production':
    from .production import *

if APP_ENV == 'test':
    from .test import *

