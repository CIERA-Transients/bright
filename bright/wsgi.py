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
os.environ['BRIGHT_DATABASE_NAME'] = ""
os.environ['BRIGHT_USER'] = ""
os.environ['BRIGHT_PASSWORD'] = ""
os.environ['BRIGHT_HOST'] = ""
os.environ['BRIGHT_PORT'] = ""

application = get_wsgi_application()
