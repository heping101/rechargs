# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  Django settings for recharge project.

  Generated by 'django-admin startproject' using Django 1.10.3.

  For more information on this file, see
  https://docs.djangoproject.com/en/1.9/topics/settings/

  For the full list of settings and their values, see
  https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

D_APP_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# 我们自己的存储根目录
STORAGE_ROOT = os.path.join(D_APP_ROOT, 'storage')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1&%iu649bdmi-fjfy&&t^r&d*o)*ag=qi2+@8lj1r(ln5l06x%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


ADMINS = (
)

# E-mail address that error messages come from.
SERVER_EMAIL = 'kaimu.tv <no-reply@runfast.tv>'

# Default e-mail address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = 'kaimu.tv <no-reply@runfast.tv>'

# Whether to use the "Etag" header. This saves bandwidth but slows down performance.
USE_ETAGS = False

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
INTERNAL_IPS = ('127.0.0.1', )

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yuan.contrib.console',
    'yuan.contrib.crashlog',
    'daterange_filter',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'yuan.contrib.crashlog.middleware.CrashLogMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'yuan.middleware.StripWhitespaceMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'xylive.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(D_APP_ROOT, 'templates'),
            os.path.join(D_APP_ROOT, 'vendor/apps/yuan/contrib/console/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'yuan.http.context_processors.siteinfo',
            ],
        },
    },
]

# WSGI_APPLICATION = 'xylive.wsgi.application'


# A dictionary mapping "app_label.model_name" strings to functions that take a
# model object and return its URL. This is a way of overriding get_absolute_url()
# methods on a per-installation basis. Example:
# ABSOLUTE_URL_OVERRIDES = {
#     'blogs.weblog': lambda o: "/blogs/%s/" % o.slug,
#     'news.story': lambda o: "/stories/%s/%s/" % (o.pub_year, o.slug),
#     'auth.user': lambda o: "/profiles/%s/" % o.username,
# }
ABSOLUTE_URL_OVERRIDES = {}

# Whether to append trailing slashes to URLs.
APPEND_SLASH = True

# Whether to prepend the "www." subdomain to URLs that don't have it.
PREPEND_WWW = False

# Override the server-derived value of SCRIPT_NAME
FORCE_SCRIPT_NAME = ''

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'runfast',
        'USER': 'runfast',
        'PASSWORD': 'runfast',
        'HOST': 'xxxx',
        'PORT': '3306',
    },
    'OPTIONS': {'charset': 'utf8', 'init_command': 'SET storage_engine=InnoDB'},
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

LANGUAGE_COOKIE_NAME = 'xylive'

LANGUAGES = (
    ('zh-cn', u'简体中文'),
    ('en', u'English'),
    # ('zh-cn', ugettext('Simplified Chinese')),
    # ('en', ugettext('English')),
)

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = False

USE_TZ = True

USE_X_FORWARDED_HOST = True


# --------------------------------------
# CACHE
# --------------------------------------

CACHE_PAGE_CACHE_ALIAS = 'pagecache'   # 页面缓存独立缓存器
CACHE_DATA_STORE_ALIAS = 'datacache'   # 数据缓存
CACHE_LIVE_DATA_ALIAS = 'livecache'    # 直播数据缓存

CACHE_VISIT_STAT_ALIAS = 'statcache'   # 访问量统计记录
CACHE_VISIT_STAT_PERIOD = 28800        # 8小时内的重复访问不做记录

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'mc.demodemo.cc:11211',
        'TIMEOUT': 86400,
        'KEY_PREFIX': 'XYLIVE'
    },
    CACHE_PAGE_CACHE_ALIAS: {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'mc.demodemo.cc:6379:1',
        'TIMEOUT': 86400,
        'KEY_PREFIX': 'XYLIVE',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 'IGNORE_EXCEPTIONS': True,
            # 'PASSWORD': 'secretpassword',  # Optional
        },
    },
    CACHE_DATA_STORE_ALIAS: {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'mc.demodemo.cc:6379:2',
        'TIMEOUT': 86400,
        'KEY_PREFIX': 'XYLIVE',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 'IGNORE_EXCEPTIONS': True,
            # 'PASSWORD': 'secretpassword',  # Optional
        },
    },
    CACHE_LIVE_DATA_ALIAS: {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'mc.demodemo.cc:6379:3',
        'TIMEOUT': 31536000,
        'KEY_PREFIX': 'XYLIVE',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 'IGNORE_EXCEPTIONS': True,
            # 'PASSWORD': 'secretpassword',  # Optional
        },
    },
    CACHE_VISIT_STAT_ALIAS: {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'mc.demodemo.cc:6379:4',
        'TIMEOUT': 86400,
        'KEY_PREFIX': 'XYLIVE',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 'IGNORE_EXCEPTIONS': True,
            # 'PASSWORD': 'secretpassword',  # Optional
        },
    },
}

CACHE_MIDDLEWARE_ALIAS = CACHE_PAGE_CACHE_ALIAS

# CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

CACHE_MIDDLEWARE_KEY_PREFIX = 'XYLIVE'

CACHE_MIDDLEWARE_SECONDS = 86400

# Ignore exceptions globally like Memcached exceptions behavior

DJANGO_REDIS_IGNORE_EXCEPTIONS = True

# --------------------------------------
# SESSIONS
# --------------------------------------

SESSION_COOKIE_NAME = 'sessionid'         # Cookie name. This can be whatever you want.
SESSION_COOKIE_AGE = 3600 * 24 * 30       # Age of cookie, in seconds (default: 1 month).
SESSION_COOKIE_DOMAIN = None              # A string like ".lawrence.com", or None for standard domain cookie.
SESSION_COOKIE_SECURE = False             # Whether the session cookie should be secure (https:// only).
SESSION_SAVE_EVERY_REQUEST = False        # Whether to save the session data on every request.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True    # Whether sessions expire when a user closes his browser.
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Default content type and charset to use for all HttpResponse objects, if a
# MIME type isn't manually specified. These are used to construct the
# Content-Type header.
DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET = 'utf-8'

# Encoding of files read from disk (template and initial SQL files).
FILE_CHARSET = 'utf-8'

# 网站对外域名
SITE_URL = 'http://ap.runfast.cn/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(STORAGE_ROOT, 'static/')
STATIC_URL = '//s1.imgcdn.demodemo.cc/www/live/'
STATIC_URL_SHARE_HTLM = 'http://s1.imgcdn.demodemo.cc/www/live/'


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(STORAGE_ROOT, 'assets/')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = 'http://img.runfast.cn/assets/'

# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # i.e. 10.0 MB

# Directory in which upload streamed files will be temporarily saved. A value of
# `None` will make Django use the operating system's default temporary directory
# (i.e. "/tmp" on *nix systems).
FILE_UPLOAD_TEMP_DIR = None

# The numeric mode to set newly-uploaded files to. The value should be a mode
# you'd pass directly to os.chmod; see http://docs.python.org/lib/os-file-dir.html.
FILE_UPLOAD_PERMISSIONS = 0644

# ---------------------------------------
# AUTHENTICATION
# ---------------------------------------

AUTHENTICATION_BACKENDS = ('yuan.contrib.console.backends.ConsoleModelBackend',
                           'django.contrib.auth.backends.ModelBackend',)

LOGIN_URL = '/console/'

LOGIN_REDIRECT_URL = '/console/'

REDIRECT_FIELD_NAME = 'next'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# --------------------------------------
# Site info
# --------------------------------------

SITEINFO_NAME = u'runfast'
SITEINFO_URL = u'https://ap.runfast.cn'
SITEINFO_DOMAIN = u'runfast.cn'
SITEINFO_SUBTITLE = u"我们所命定的目标，不是享乐，不是受苦，而是行动，在每一个明天，都要比今天前进一步。"


# --------------------------------------
# apple pay相关配置
# --------------------------------------
APPLE_PAY_VERIFY_RECEIPT_URL = 'https://buy.itunes.apple.com/verifyReceipt'

# --------------------------------------
# 主播配置
# --------------------------------------
WITHDRAW_RATIO = 0.9                        # 提现比例：0.9表示10金券提0.9元


# --------------------------------------
# 加载本地标识 me.py 文件
# --------------------------------------

try:
    from recharge.config import me
    MY_HOST_IDENT = me._HOST_IDENT
except:
    raise Exception("Can not identify my IDENT, setup it in local xylive/config/me.py file first!")

# --------------------------------------
# 根据 me.py 文件中标识，加载对应的本地化配置文件
# --------------------------------------

try:
    config_module = __import__('recharge.config.%s' % me._HOST_IDENT, globals(), locals(), 'recharge')
    # Load the config settings properties into the local scope.
    for setting in dir(config_module):
        if setting == setting.upper():
            locals()[setting] = getattr(config_module, setting)
except ImportError:
    import sys
    sys.stderr.write("""Error: Can't find the file 'recharge/config/%s.py' in the directory containing %r. """
                     """It appears you've customized things.\n"""
                     """(If the file recharge/config/%s.py does indeed exist, it's causing an ImportError somehow.)\n""" %
                     (me._HOST_IDENT, me._HOST_IDENT, __file__))
    sys.exit(1)


# --------------------------------------
# Logging - 需要根据DEBUG开关确定日志记录级别
# --------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'http_logfile': {
            'level': 'DEBUG',
            'class': 'yuan.logging.handlers.RotatingFileWithOwnerHandler',
            'filename': os.path.join(D_APP_ROOT, "logs/apps", "django-http.log"),
            'maxBytes': 50000000,
            'backupCount': 2,
            'formatter': 'standard',
            'uid': 80,
            'gid': 80,
        },
        'db_logfile': {
            'level': 'DEBUG',
            'class': 'yuan.logging.handlers.RotatingFileWithOwnerHandler',
            'filename': os.path.join(D_APP_ROOT, "logs/apps", "django-db.log"),
            'maxBytes': 50000000,
            'backupCount': 2,
            'formatter': 'standard',
            'uid': 80,
            'gid': 80,
        },
        'debug_logfile': {
            'level': 'DEBUG',
            'class': 'yuan.logging.handlers.RotatingFileWithOwnerHandler',
            'filename': os.path.join(D_APP_ROOT, "logs/apps", "debug.log"),
            'maxBytes': 50000000,
            'backupCount': 2,
            'formatter': 'standard',
            'uid': 80,
            'gid': 80,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['http_logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['db_logfile'],
            'level': DEBUG and 'DEBUG' or 'INFO',
            'propagate': False,  # django also has database level logging
        },
        'debug.all': {
            'handlers': ['debug_logfile'],
            'level': DEBUG and 'DEBUG' or 'INFO',
            'propagate': False,  # django also has database level logging
        },
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # }
    }
}
