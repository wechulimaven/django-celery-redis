from celery import shared_task

from django
@shared_task(bind=True)
def test_func(self):
    # operations
    for i in range(10):
        print(i)
    return 'Done'