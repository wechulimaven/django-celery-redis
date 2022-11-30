from django.http import HttpResponse
from mainapp.tasks import test_func

# Create your views here.

def test_fn(request):
    test_func.delay()
    return HttpResponse('task done')