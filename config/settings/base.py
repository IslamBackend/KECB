import os

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from .jazzmin import *

from .env_reader import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PRODUCTION = env('PRODUCTION', default=False, cast=bool)

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THEME_APPS = [
    "modeltranslation",
    'jazzmin'
]

LIBRARY_APPS = [
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'django_summernote',
]

LOCAL_APPS = [
    'apps.common.apps.CommonConfig',
    'apps.announcement.apps.AnnouncementConfig',
    'apps.center_info.apps.CenterInfoConfig',
    'apps.center_courses.apps.CenterCoursesConfig',
    'apps.korean_edu.apps.KoreanEduConfig',
    'apps.library.apps.LibraryConfig',
    'apps.home.apps.HomeConfig',
]

INSTALLED_APPS = [
    *THEME_APPS,
    *DJANGO_APPS,
    *LIBRARY_APPS,
    *LOCAL_APPS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

gettext = lambda s: s

LANGUAGES = [
    ("ru", _("Русский")),
    ("ko", _("Korean")),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'center_info/locale'),
]

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'back_static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'back_media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%d.%m.%Y",
    'DATE_FORMAT': "%d.%m.%Y",
}

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'width': '600',
        'height': '500',
    },
}

if not PRODUCTION:
    from .development import *
else:
    from .production import *

if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
