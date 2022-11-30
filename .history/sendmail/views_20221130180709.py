from django.http import HttpResponse
from sendmail.tasks import send_mail_func

# Create your views here.
def send_mail(request):
    send_mail_func.delay()
    return HttpResponse('Mail send')

def schedule_mail_dynamically(request):
    schedule,created=Ce