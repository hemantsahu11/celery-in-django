from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
# Create your views here.


def test(request):
    print("test count function")
    test_func.delay()
    print("request")
    return HttpResponse('Done')


def home(request):
    return HttpResponse("Celery Home")


def send_main_to_all(request):
    print("send mail to all function")
    send_mail_func.delay()    # apply async and give countdown
                                # retry's in celery
    return HttpResponse("sent")
