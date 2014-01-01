# Django settings for sjchurch project.
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT= os.path.abspath(os.path.dirname(BASE_DIR))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if 'HEROKU' in os.environ:
    
    #AWS_QUERYSTRING_AUTH = False
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_PRELOAD_METADATA = True # necessary to fix manage.py collectstatic command to only upload changed files instead of all files
    S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    
    HEROKU_DEBUG= os.environ.get('HEROKU_DEBUG', False)
    if(HEROKU_DEBUG=='True'):
        DEBUG= True
        TEMPLATE_DEBUG = DEBUG
#         STATIC_ROOT = 'staticfiles'
#         STATIC_URL = '/static/'
#     else:
#         DEBUG= False
#         STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#         STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/staticfiles/'
       
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_S3_PATH = "media"
    MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
    ADMIN_MEDIA_PREFIX= 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES = { 'default': dj_database_url.config()}
    
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/' #THIS WORKS WHEN DEBUG= TRUE BUT NOT WHEN FALSE!
#    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#    MEDIA_URL = '/media/'

    #AWS_QUERYSTRING_AUTH = False
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_PRELOAD_METADATA = True # necessary to fix manage.py collectstatic command to only upload changed files instead of all files

    S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    #STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    #STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    #STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
       
    #DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = "media"
    #STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    #STATIC_S3_PATH = "static"
    MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
    
    MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    
    #STATIC_ROOT = "/%s/" % STATIC_S3_PATH
    
    #ADMIN_MEDIA_PREFIX= 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'sjchurch',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'michael',
            'PASSWORD': 'kandj1001',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }           
    }

ALLOWED_HOSTS = ['*']
TIME_ZONE = 'GB'
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]
SITE_ID = 1

USE_I18N = False
USE_L10N = True
USE_TZ = True

#FILER_ENABLE_PERMISSIONS= True

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
    os.path.join(PROJECT_ROOT, 'audio/static'),
    os.path.join(PROJECT_ROOT, 'slideshow/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o20(#=e^@cy1494dxrmdvf@8fmx7r(6t9qtp_4$*gmtmb6e9-q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'zinnia.context_processors.version', # this is optional for zinnia
)

CMS_TEMPLATES = (
    ('2_panels.html', 'Home Template 2 panels'),
    ('3_panels.html', 'Home Template 3 panels'),  
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'sjchurch.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sjchurch.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

FILER_IMAGE_USE_ICON= True
TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_MAX_PAGE_PUBLISH_REVERSIONS= 3

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'djangocms_text_ckeditor',
    
    'cms',
    'cms.stacks',
    #'cms.plugins.picture',
    'cms.plugins.link',
    'cmsplugin_filer_image',
    'cmsplugin_zinnia',
    'cms.plugins.googlemap',

    'mptt',
    'south',
    'sekizai',
    'menus',
    'filer',
    'easy_thumbnails',
    'reversion',
    'tagging',
    'zinnia',

    'audio',
    'carousel',
    'documents',
    'events',
    'news',
    'people',   
    'slideshow',
    
    'gunicorn',
    'storages',
    'boto',
    's3_folder_storage',
    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
