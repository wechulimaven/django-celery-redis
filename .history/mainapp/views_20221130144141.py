from django.shortcuts import render

# Create your views here.

def test_fn(request):
    return HttpResponse('task done')