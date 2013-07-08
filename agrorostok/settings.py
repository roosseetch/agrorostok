# Django settings for agrorostok project.

import os

SETTINGS_ROOT = os.path.dirname(__file__).replace('\\', '/')
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

DEBUG = True
TEMPLATE_DEBUG = True
SQL_DEBUG = True
SEND_BROKEN_LINK_EMAILS = False
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

CACHES = {
    'default': {
        'BACKEND':
        'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

LANGUAGES = (
    ('en-gb', 'English'),
    ('ru-RU', 'Russian'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATIC_ROOT = os.path.join(os.path.dirname(SETTINGS_ROOT), "static/").replace('\\', '/')
# STATIC_ROOT = os.path.join(os.path.dirname(SETTINGS_ROOT), "static/")
STATIC_ROOT = os.path.join(SETTINGS_ROOT, "../static/")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # os.path.join(os.path.dirname(SETTINGS_ROOT), "istore/static/"),
    os.path.join(SETTINGS_ROOT, "../istore/static/"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't9rr%mbyc^9%za@&d(jb-l$8^y+01zydy=+ld-ba&@hde34w(b'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    # istore specific
    # 'oscar.apps.search.context_processors.search_form',
    'istore.apps.promotions.context_processors.promotions',
    'istore.apps.checkout.context_processors.checkout',
    'istore.core.context_processors.metadata',
    'istore.apps.customer.notifications.context_processors.notifications',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'istore.apps.basket.middleware.BasketMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'agrorostok.urls'

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'agrorostok.wsgi.application'

from istore import ISTORE_MAIN_TEMPLATE_DIR
# TEMPLATE_DIRS =(os.path.join(os.path.dirname(SETTINGS_ROOT), 'templates').replace('\\','/'),)
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(SETTINGS_ROOT), 'templates'),
    ISTORE_MAIN_TEMPLATE_DIR,
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s\n\n'
        },
        'simple': {
            'format': '%(levelname)s %(message)s\n\n'
        },
    },
    'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'checkout_file': {
             'level': 'INFO',
             'class': 'istore.core.logging.handlers.EnvFileHandler',
             'filename': 'checkout.log',
             'formatter': 'verbose'
        },
        'error_file': {
             'level': 'INFO',
             'class': 'istore.core.logging.handlers.EnvFileHandler',
             'filename': 'errors.log',
             'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'istore.checkout': {
            'handlers': ['console', 'checkout_file'],
            'propagate': True,
            'level':'INFO',
        },
        'django.db.backends': {
            'handlers':['null'],
            'propagate': False,
            'level':'DEBUG',
        },
    }
}


INSTALLED_APPS = (
    'admintools_bootstrap',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # Oscar dependencies
    'compressor',
    'south',
    # Agrorostok extensions
    'istore',
    'agrorostok',
    'istore.apps.analytics',
    'istore.apps.order',
    'istore.apps.checkout',
    'istore.apps.shipping',
    'istore.apps.catalogue',
    'istore.apps.catalogue.reviews',
    'istore.apps.basket',
    # 'istore.apps.payment',
    'istore.apps.offer',
    'istore.apps.address',
    # 'istore.apps.partner',
    'istore.apps.customer',
    'istore.apps.promotions',
    # 'istore.apps.search',
    'istore.apps.voucher',
    'istore.apps.dashboard',
    'istore.apps.dashboard.reports',
    'istore.apps.dashboard.users',
    'istore.apps.dashboard.orders',
    'istore.apps.dashboard.promotions',
    'istore.apps.dashboard.catalogue',
    'istore.apps.dashboard.offers',
    'istore.apps.dashboard.ranges',
    'istore.apps.dashboard.vouchers',
    'istore.apps.dashboard.communications',
    # External apps
    'django_extensions',
    'debug_toolbar',
    # 3rd-party apps that oscar depends on
    # 'haystack',
    'treebeard',
    'sorl.thumbnail',
    # For profile testing
    'istore.apps.user',
    'istore.apps.bigbang',
)

# from istore import get_core_apps
# INSTALLED_APPS = INSTALLED_APPS + get_core_apps(['apps.shipping'])

# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Include a shipping override app to provide some shipping methods

AUTHENTICATION_BACKENDS = (
    'istore.apps.customer.auth_backends.Emailbackend',
    # 'auth.authentication.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/accounts/'
APPEND_SLASH = True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# AUTH_PROFILE_MODULE = 'user.Profile'

# istore settings
from istore.defaults import *

ISTORE_RECENTLY_VIEWED_PRODUCTS = 20
ISTORE_ALLOW_ANON_CHECKOUT = True

ISTORE_SHOP_NAME = 'Agrorostok'
ISTORE_SHOP_TAGLINE = 'Official site'

#GOOGLE_ANALYTICS_ID = 'UA-XXXXX-Y'

COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

THUMBNAIL_KEY_PREFIX = 'Agrorostok official'

LOG_ROOT = location('logs')
# Ensure log root exists
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)

DISPLAY_VERSION = False

# Must be within MEDIA_ROOT for sorl to work
ISTORE_MISSING_IMAGE_URL = 'image_not_found.jpg'

# Add stores node to navigation
new_nav = ISTORE_DASHBOARD_NAVIGATION
new_nav.append(
    {
        'label': 'Stores',
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': 'Stores',
                'url_name': 'stores-dashboard:store-list',
            },
            {
                'label': 'Store groups',
                'url_name': 'stores-dashboard:store-group-list',
            },
        ]
    })
new_nav.append(
    {
        'label': 'Datacash',
        'icon': 'icon-globe',
        'children': [
            {
                'label': 'Transactions',
                'url_name': 'datacash-transaction-list',
            },
        ]
    })
ISTORE_DASHBOARD_NAVIGATION = new_nav

# GEOIP_PATH = os.path.join(os.path.dirname(__file__), 'geoip')
