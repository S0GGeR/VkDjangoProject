import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'D1lXPO4k30mEB242dgw2SRfSMuMVITs4xGzjg1h5pF3ZMDo0gmwB'
DEBUG = False
ALLOWED_HOSTS = ['35.228.153.157', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vk_auth',
        'USER': 'sogger_tur',
        'PASSWORD': 'sgw2Sfs2451GJUF',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')