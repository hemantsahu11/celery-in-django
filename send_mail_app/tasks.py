from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from core import settings
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_mail_func():
    print("task send mail function")
    users = get_user_model().objects.all()
    for user in users:
        print(user)
        mail_subject = 'Hi! project Testing'
        message = "This is test mail for Hemant django project"
        to_email = user.email
        print(user.email)
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )
    return "Email Sent"
