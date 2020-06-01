

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SendGrid Email



ALLOWED_HOSTS = ['sentheard.pythonanywhere.com',
'www.sentheard.com']

AUTH_USER_MODEL = 'users.CustomUser'


# Application definition

INSTALLED_APPS = [
    'Sent_Heard_App',
    'posts.apps.PostsConfig',
    'users.apps.UsersConfig',
    'payments.apps.PaymentsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'always_authenticated.middleware.AlwaysAuthenticatedMiddleware',
]

# To run the middleware in production, set ALWAYS_AUTHENTICATED_DEBUG_ONLY to False.
ALWAYS_AUTHENTICATED_DEBUG_ONLY = False


ROOT_URLCONF = 'sent_heard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['templates',],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'sent_heard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'sentheard$sentheard-db2',
    'USER': 'sentheard',
    'PASSWORD': 'MsQL2019@!jw*aw3',
    'HOST': 'sentheard.mysql.pythonanywhere-services.com',
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# USE_S3 = os.getenv('USE_S3') == 'TRUE'

# if USE_S3:
#     # aws settings
#     AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
#     # add to os.environ
#     AWS_STORAGE_BUCKET_NAME = 'django-static-sentheard'
#     AWS_S3_REGION_NAME = 'us-east-2'
#     AWS_DEFAULT_ACL = 'public-read'
#     AWS_QUERYSTRING_AUTH = False
#     AWS_IS_GZIPPED = True
#     AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
#     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#     PUBLIC_MEDIA_LOCATION = '/media'
#     # Perhaps add Region ID
#     MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
#     # DEFAULT_FILE_STORAGE = 'sent_heard.storage_backends.PublicMediaStorage'
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# else:
#     MEDIA_URL = '/media/'
#     MEDIA_ROOT = os.path.join(BASE_DIR, '/media')
THUMBNAIL_HIGH_RESOLUTION = True


PROJECT_URL = 'https://www.sentheard.com'

MEDIA_URL = '/'
MEDIA_ROOT = '/home/sentheard/sentheard/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')



# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_URL = 'static/'
STATIC_ROOT = '/home/sentheard/sentheard/static/'


# SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

LOGIN_REDIRECT_URL = '../../post_stuff/gallery/'
LOGOUT_REDIRECT_URL = 'index'



EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Sentheard.Mgmt@gmail.com'
# EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")
EMAIL_HOST_PASSWORD = 'sbdwxeovihqiygdt'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'SentHeard Team <noreply@sentheard.com>'

# Your app password for your device
#   sbdwxeovihqiygdt

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
SENDGRID_ECHO_TO_STDOUT=True
# Toggle sandbox mode (when running in DEBUG mode)
# SENDGRID_SANDBOX_MODE_IN_DEBUG=True

# echo to stdout or any other file-like object that is passed to the backend via the stream kwarg.


STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")



# Subscriptions
DFS_CURRENCY_LOCALE = 'en_us'

# Subscriptions
DFS_BASE_TEMPLATE = 'index.html'



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]