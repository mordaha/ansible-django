"""
WSGI config for project project.
"""

import os
import dotenv

dotenv.read_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
