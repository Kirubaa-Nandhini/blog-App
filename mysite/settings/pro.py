import os
import dj_database_url
from .base import *

DEBUG = False

ADMINS = (
    ('testpress', 'kirubaanandhini@testpress.in'),
)

ALLOWED_HOSTS = ['.onrender.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600
    )
}

SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
