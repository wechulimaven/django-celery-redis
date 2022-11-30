from django.http import HttpResponse
from django.shortcuts import render
from 

# Create your views here.

def test_fn(request):

    return HttpResponse('task done')