from .base import *
DEBUG = False
ADMINS = (
 ('testpress', 'kirubaanandhini@testpress.in'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite',
        'USER': 'blogs',
        'PASSWORD': 'testpress',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

