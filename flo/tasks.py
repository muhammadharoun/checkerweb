from celery import task
from .reverse_scrap import final_task
from .traker import run_tracker

@task
def work_now2():
    try:
        final_task()
    except:
        pass
    
    try:
        run_tracker()
    except:
        pass
    return True
