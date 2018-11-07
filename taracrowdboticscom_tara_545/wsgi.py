"""
WSGI config for taracrowdboticscom_tara_545 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taracrowdboticscom_tara_545.settings")

application = get_wsgi_application()
