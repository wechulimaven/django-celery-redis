from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.test_fn, name='test')
]
