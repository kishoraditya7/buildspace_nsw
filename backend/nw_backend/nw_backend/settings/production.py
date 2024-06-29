from .base import *

DEBUG = False
# Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


import environ

env = environ.Env()
environ.Env.read_env()  # reads the .env file

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

#import os
#import dj_database_url

# ... other settings ...

#DATABASES = {
#    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
#}
try:
    from .local import *
except ImportError:
    pass
