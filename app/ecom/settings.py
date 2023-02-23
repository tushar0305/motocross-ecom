import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xvgs%g09_ph)$z+hwy8=_txh8hr--7^%pp*4k47*w_mbc5)g=8'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','103.174.149.31','www.mymotokart.com','mymotokart.com']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'store',
    'basket',
    'django_countries',
    'payment',
    'orders',
    'django_filters',

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

ROOT_URLCONF = 'ecom.urls'

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
                'store.context_processors.all_companies',
                'store.context_processors.all_bikes',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecom.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/db.sqlite3',
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

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
#STATIC_ROOT=BASE_DIR/'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BASKET_SESSION_ID = 'basket'
SHOP_APP_LABEL = ''

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# user Model settings
AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login'

# Payment Setup
# Paytm Setup
PAYTM_MERCHANT_ID = 'merchant_id>'
PAYTM_SECRET_KEY = 'paytm_secret_key>'
PAYTM_WEBSITE = 'WEBSTAGING'
PAYTM_CHANNEL_ID = 'WEB'
PAYTM_INDUSTRY_TYPE_ID = 'Retail'
# Razorpay Setup
RAZOR_KEY_ID = "rzp_test_nCmjr7rmkAfyLn"
RAZOR_KEY_SECRET = "oTR2wjEMWTdVeouHhXxtxVRC"

# Email Setup
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

"""EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'onkart4u@gmail.com'
EMAIL_HOST_PASSWORD = 'onkartodkar043@gmail.com'"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = 'mail.motocrossindia.in'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'motokart@motocrossindia.in'
EMAIL_HOST_PASSWORD = 'motokart@moto'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

PASSWORD_RESET_TIMEOUT_DAYS = 7

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Motocross Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": " ",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "MOTOCROSS",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "/small_logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "/small_logo.png",

    # following line activates interactive colour and ui changes for jazzmin theme
    "show_ui_builder": True
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "darkly",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,

    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": False

}

# Additional options to add
# Theme changing options
"""
JAZZMIN_UI_TWEAKS = {
    "theme": "cyborg",
}

options for theme are
Light themes
    default (Standard theme built on top of bootstrap)
    cerulean preview
    cosmo preview
    flatly preview
    journal preview
    litera preview
    lumen preview
    lux preview
    materia preview
    minty preview
    pulse preview
    sandstone preview
    simplex preview
    sketchy preview
    spacelab preview
    united preview
    yeti preview

Dark themes¶

    darkly preview
    cyborg preview
    slate preview
    solar preview
    superhero preview
"""
