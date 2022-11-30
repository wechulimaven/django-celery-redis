from django.http import HttpResponse
from sendmail.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule


# Create your views here.
def send_mail(request):
    send_mail_func.delay()
    return HttpResponse('Mail send')

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")

