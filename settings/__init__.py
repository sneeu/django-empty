import os
import sys


SERVER_ENV = os.environ.get('SERVER_ENV', 'development')

DEBUG = TEMPLATE_DEBUG = (SERVER_ENV == 'development')

SITE_ID = 1
SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

TIME_ZONE = 'Europe/London'
DATE_FORMAT = 'j F y'
TIME_FORMAT = 'P'
DATETIME_FORMAT = ', '.join([TIME_FORMAT, DATE_FORMAT])
MONTH_DAY_FORMAT = 'j F'
LANGUAGE_CODE = 'en-gb'

EMAIL_SUBJECT_PREFIX = '[Refresh Edinburgh] '

ROOT_URLCONF = 'urls'

USE_ETAGS = False

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

TEMPLATE_DEBUG = DEBUG
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'apps.core.context_processors.media_url',
    'apps.core.context_processors.current_site',
)
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates/'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.admin',

    'debug_toolbar',

    'apps.core',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


settings = __import__('settings.%s' % SERVER_ENV, globals(), locals(), ['*'])
for s in dir(settings):
    if s == s.upper():
        setattr(sys.modules[__name__], s, getattr(settings, s))
