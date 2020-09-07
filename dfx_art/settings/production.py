import os

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*'] 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SECURITY WARNING: keep the secret key used in production secret!

try:
    from .local import *
except ImportError:
    pass

print('App configuration: production')