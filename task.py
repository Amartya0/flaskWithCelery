from array import array
import numbers
from celery import Celery
import time

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@celery.task
def addition(x, y):
    time.sleep(1)
    return x + y

@celery.task
def sub(x, y):
    time.sleep(20)
    return x - y

@celery.task
def a_min(n:numbers):
    for i in range(n):
        time.sleep(1)
    return (f'Done waiting')

@celery.task
def pnt(str:array):
    return sum(str)
