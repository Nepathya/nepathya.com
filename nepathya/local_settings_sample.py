from settings import *

SECRET_KEY = '=s0$)ng6s4x@tt=e+v3hygikjuwn3d_m1ihz$m07e(g#bhj)xz'

# ADMINS = [('Milan Tamang', 'milan.tamang@tgsolutions.co')]
# SERVER_EMAIL = 'webmaster@mzoom.mtradeasia.com'

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# ALLOWED_HOSTS = ['mtradeasia.com', 'mzoom.mtradeasia.com', 'localhost', '127.0.0.1']

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, '..', 'emails')