import os
from pathlib import Path

from django.conf.global_settings import MEDIA_URL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u1g%=dhr)5_sj#sq02o#9f%-1=l+04(luvq)f(^e^p7wp=1c8@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

CART_SESSION_ID = 'cart'

EMAIL_HOST_USER = 'viowolf050104@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
CELERY_BROKER_URL = "redis://" + REDIS_HOST + ":" + str(REDIS_PORT) + "/0"
CELERY_RESULT_BACKEND = "redis://" + REDIS_HOST + ":" + str(REDIS_PORT) + "/0"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

STRIPE_PUBLISHABLE_KEY = 'pk_test_51RAD1GFNtrvWvY6VCgv4XTxfd1BuPsR7a2DSRxvyjLiFYF0FZhq46KUBMvFHogSCEqCEpfbLKw18dhLgT9Hb9DK600MYSrTFdi'
STRIPE_SECRET_KEY = 'sk_test_51RAD1GFNtrvWvY6VTWNdhn3d8zIj4uyc2O0VxNg7adUS9R78xQ1yWBaJ8SKp4H5Z98elwfChIp6kVTWGopXFuOwm00Ngm3Reb8'
STRIPE_API_VERSION = '2022-08-01'
STRIPE_WEBHOOK_SECRET = 'whsec_349fb751582f61427fe8ede8d675ec3751147f4aa713c56d4f81468543e439f6'
