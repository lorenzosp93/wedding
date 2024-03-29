"""
Django settings for wedding project.
"""

import os

AUTH_USER_MODEL = 'auth.User'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '17cgw1@w%hm%a#2$z7v^$(e=+=8q)unx4!v_-q+&nd0omm$)9('
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    '17cgw1@w%hm%a#2$z7v^$(e=+=8q)8nx4!3_-q+&nd0omm$)9(',
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '') != 'False'

HOST = os.environ.get('DJANGO_HOST', None)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',  # local debugging
    ]

if HOST:
    ALLOWED_HOSTS.append('.' + HOST)
    CSRF_TRUSTED_ORIGINS = ['https://' + HOST]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shared',
    'inbox',
    'info',
    'profile',
    'guestbook',
    'wedding',
    'storages',
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
    'rest_framework',
    'rest_framework.authtoken',
    'drfpasswordless',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'wedding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
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

WSGI_APPLICATION = 'wedding.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DATABASE_NAME', 'db.sqlite3'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', 5432)
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

X_FRAME_OPTIONS = 'DENY'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# The URL to use when referring to static files
# (where they will be served from)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

USE_S3 = os.getenv('USE_S3') == 'True'

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # AWS_IS_GZIPPED = True
    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'wedding.custom_storages.StaticStorage'
    # s3 public media settings
    MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'wedding.custom_storages.MediaStorage'
else:
    STATIC_URL = '/staticfiles/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/mediafiles/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'shared.authentication.ExpiringTokenAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/minute',
        'user': '50/minute',
    }
}
if not DEBUG:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
        "rest_framework.renderers.JSONRenderer",
    )
TOKEN_EXPIRED_AFTER_SECONDS = 60 * 60 * 24 * 30  # 30 days tokens expiry

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True

BACKEND_HOST = os.environ.get(
    'BACKEND_HOST') if not DEBUG else 'http://localhost:8000'
FRONTEND_HOST = os.environ.get('FRONTEND_HOST', 'http://localhost:8080')

PASSWORDLESS_AUTH = {
    'PASSWORDLESS_AUTH_TYPES': ['EMAIL', ],
    'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': os.environ.get('EMAIL_TO', 'info@priscillalorenzo.com'),
    'PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME': "token_email.html",
    'PASSWORDLESS_EMAIL_CALLBACK': 'shared.utils.send_email_with_callback_token',
    'PASSWORDLESS_REGISTER_NEW_USERS': False,
    'PASSWORDLESS_TOKEN_EXPIRE_TIME': 15 * 60,
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_TO = os.environ.get('EMAIL_TO', 'info@priscillalorenzo.com')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', "True") == "True"

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": os.environ.get('WEB_PUSH_PUBLIC_KEY'),
    "VAPID_PRIVATE_KEY": os.environ.get('WEB_PUSH_PRIVATE_KEY'),
    "VAPID_ADMIN_EMAIL": os.environ.get('WEB_PUSH_ADMIN_EMAIL', "me@lorenzosp.com"),
}

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_USER = os.environ.get('REDIS_USER', '')
REDIS_PASS = os.environ.get('REDIS_PASSWORD', '')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_TASK_DB = 0
REDIS_CACHE_DB = 1

REDIS_AUTH = f'{REDIS_USER}:{REDIS_PASS}@' if REDIS_PASS else ''

CELERY_BROKER_URL = f"redis://{REDIS_AUTH}{REDIS_HOST}:{REDIS_PORT}/{REDIS_TASK_DB}"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Amsterdam'

REDIS_URL = f"redis://{REDIS_AUTH}{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}"

if not DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
CACHE_TTL = 60 * 60  # 1 hour
