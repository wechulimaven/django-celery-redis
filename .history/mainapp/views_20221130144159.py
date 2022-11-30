from django.http import HttpResponse
from django.shortcuts import render
from .tasks import 

# Create your views here.

def test_fn(request):

    return HttpResponse('task done')