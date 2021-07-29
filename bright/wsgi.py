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
os.environ['BRIGHT_DATABASE_NAME'] = "bright"
os.environ['BRIGHT_USER'] = "bright"
os.environ['BRIGHT_PASSWORD'] = "brightadmin"
os.environ['BRIGHT_HOST'] = "bright.ciera.northwestern.edu"
os.environ['BRIGHT_PORT'] = "5432"

application = get_wsgi_application()
