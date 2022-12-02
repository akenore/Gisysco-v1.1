from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import constants as messages
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = True
SITE_ID = 1
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'compressor',
    'notifications',
    'sorl.thumbnail',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',
    'ckeditor_uploader',
    # Apps
    'frontend',
    'client',

]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Español')),

]
LOCALE_PATHS = [BASE_DIR / 'locale']
CORS_ORIGIN_ALLOW_ALL = True


STATIC_URL = '/static/'
MEDIA_URL = '/upload/'
MEDIA_ROOT = BASE_DIR / 'upload'
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR, 'static']
else:
    STATIC_ROOT = BASE_DIR / 'static'


COMPRESS_ROOT = BASE_DIR / 'static'
COMPRESS_ENABLED = True
STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MESSAGE_TAGS = {
    messages.DEBUG: 'text-gray-700 bg-gray-100 border-gray-500 dark:bg-gray-200',
    messages.INFO: 'text-blue-700 bg-blue-100 border-blue-500 dark:bg-blue-200',
    messages.SUCCESS: 'text-green-700 bg-green-100 border-green-500 dark:bg-green-200',
    messages.WARNING: 'text-yellow-700 bg-yellow-100 border-yellow-500 dark:bg-yellow-200',
    messages.ERROR: 'text-red-700 bg-red-100 border-red-500 dark:bg-red-200',

}

LOGIN_REDIRECT_URL = 'dashboard'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED=True
# AUTH_PROFILE_MODULE = 'client.UserInfo'
ACCOUNT_FORMS = {
    'login': 'client.forms.CustomLoginForm',
    'signup': 'client.forms.CustomSignupForm',
    'reset_password': 'client.forms.CustomResetPasswordForm',
    'change_password': 'client.forms.CustomPasswordChangeForm'
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}
