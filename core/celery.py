from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')

#Celery beat settings
# app.conf.beat_schedule = {
#     'send-mail-every-day-at-8': {
#         'task': 'send_mail_app.tasks.send_mail_func',
#         'schedule': crontab(hour=8, minute=1),  # crontab is used to schedule timing at which we have to send mail
#         'options': {'queue': 'feeds'},
#         # 'args': (2,)  # if you want to pass some argument to function
#     },
#     'run-count': {
#         'task': 'cel_app.tasks.test_func',
#         'schedule': crontab(hour=8, minute=1),
#         'options': {'queue': 'default'}
#     }
# }

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request : {self.request!r}")
