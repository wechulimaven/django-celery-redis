from django.http import HttpResponse
from sendmail.tasks import send_mail_function

# Create your views here.
def send_mail(request):
    send_mail_func.delay()
    return HttpResponse('Mail send')