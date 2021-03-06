import os

from .base import *

DEBUG = os.getenv('DEBUG', None) == 'True' or False
ALLOWED_HOSTS = ['*'] 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SECURITY WARNING: keep the secret key used in production secret!

try:
    from .local_settings import *
except ImportError:
    pass

print('App configuration: production')