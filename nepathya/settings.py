import os
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gettext = lambda s: s

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'rest_framework',
    'fcm',
    # 'rest_framework.authtoken',
    # 'linaro_django_pagination',
    # 'webstack_django_sorting',
    #
    'apps.discography',
    'apps.news',
    'apps.gallery',
    'apps.video',
    'apps.events',
    'apps.feedback',
    'apps.push_notification',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware',
    'webstack_django_sorting.middleware.SortingMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

ROOT_URLCONF = 'nepathya.urls'

WSGI_APPLICATION = 'nepathya.wsgi.application'

LANGUAGE_CODE = 'en'

# AUTH_USER_MODEL = 'users.User'
# LOGIN_URL = 'users:login'
# LOGIN_REDIRECT_URL = '/'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = False

FCM_APIKEY = "AAAAmVB3Xyo:APA91bErbKY5vOPrQaOz1tYx6VoyV34xg7FXt-lvEDBa98S11Ld0y5LPlElmT59126JLlUH77XFG8lJjAC9PgR7wI6bmpTQAmwQ2o_o6Gi5cHk7qPqAR8yiFW00Xo8XYj5mwz5Zch5LgBuGO2BNi4LtBsBG6_6lfWQ"

FCM_MAX_RECIPIENTS = 10000

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

TEMPLATE_DEBUG = True