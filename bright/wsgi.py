"""
WSGI config for bright project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bright.settings')
os.environ['HTTPS'] = "on"
os.environ['GRAVITYSPYTOOLS_NAME'] = ""
os.environ['GRAVITYSPYTOOLS_USER'] = ""
os.environ['GRAVITYSPYTOOLS_PASSWORD'] = ""
os.environ['GRAVITYSPYTOOLS_HOST'] = ""
os.environ['GRAVITYSPYTOOLS_PORT'] = ""

application = get_wsgi_application()
