from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings') #Project directorty

app = Celery('django_celery') # ADD PROJECT NAME
app.conf.enable_utc = False # Telling django to use our own written timezone

app.conf.update(timezone = 'Nairobi')


app.config_from_object(settings,namespace='CELERY') #The uppercase name-space means that all Celery configuration options must be specified in uppercase , and start with CELERY_