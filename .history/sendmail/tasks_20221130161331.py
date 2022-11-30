from celery import shared_task

from django.contrib.auth import get_user_model

@shared_task(bind=True)
def send_mail(self):
    # operations
    for i in range(10):
        print(i)
    return 'Done'