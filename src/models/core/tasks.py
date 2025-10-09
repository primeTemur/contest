from celery import shared_task
import time

@shared_task 
def add():
    time.sleep(5)    
    print('5 sekunt kutdim')
    return 0