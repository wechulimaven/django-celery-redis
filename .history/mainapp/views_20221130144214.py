from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func

# Create your views here.

def test_fn(request):
    test_func.dela
    return HttpResponse('task done')