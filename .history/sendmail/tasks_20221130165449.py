from celery import shared_task

from django.contrib.auth import get_user_model
from django.core.mail import send

@shared_task(bind=True)
def send_mail_function(self):
    users = get_user_model().objects.all()
    for user in users:
