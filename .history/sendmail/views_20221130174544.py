from django.http import HttpResponse

# Create your views here.
def send_mail(request):
    send_mail_func.delay()
    return HttpResponse('Mail send')