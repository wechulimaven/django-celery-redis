from celery import shared_task

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_celery import settings
@shared_task(bind=True)
def send_mail_function(self):
    users = get_user_model().objects.all()
    for user in users:
        # You can write a html file and convert to string and pass it here
        message = "Liking my content here we go"
        mail_subject= "Celery on the go"
        to_email = user.email
        send_mail(
            subject=mail_subject
            message=message
            from_email=settings
        )
