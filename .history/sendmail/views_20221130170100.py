from django.shortcuts import render
from .tasks import send_mail_function

# Create your views here.
def send_mail(request):
    se