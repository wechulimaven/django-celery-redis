from django.urls import path
from sendmail import views

urlpatterns = [
    path('', views.send_mail, name='send')
]
