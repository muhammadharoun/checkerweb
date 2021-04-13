import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task , task
from .reverse_scrap import final_task
from .traker import run_tracker

@task
def work_now():
    try:
        final_task()
    except:
        pass
    
    try:
        run_tracker()
    except:
        pass
    return True
