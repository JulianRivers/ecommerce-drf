from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
    conn_max_age=600    )
}