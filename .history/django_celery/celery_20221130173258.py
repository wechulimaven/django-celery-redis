from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings') #Project directory to settings file

app = Celery('django_celery') # ADD PROJECT NAME
app.conf.enable_utc = False # Telling django to use our own written timezone

app.conf.update(timezone = 'Africa/Nairobi')

#Celery beat settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8':{
'task':'sendmail.tasks.send_mail_function',
'schedule':crontab(hour=17,minute=0),
# 'args':(2,)
    }
}

app.config_from_object(settings,namespace='CELERY') #The uppercase name-space means that all Celery configuration options must be specified in uppercase , and start with CELERY_

app.autodiscover_tasks() #TO automatically discover tasks from all of your installed apps, following the tasks.py convention

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')