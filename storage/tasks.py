from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import timedelta, datetime

@shared_task
def dummy(instance):
    start = datetime.today()
    delta = timedelta(seconds=3)
    now = datetime.today()
    while (now - start) < delta:
        now = datetime.today()