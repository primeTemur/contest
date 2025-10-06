from django.shortcuts import render
from .tasks import add
import time
from django.http import HttpResponse

def index(request):
    add.delay()
    # time.sleep(5)
    return HttpResponse("Hello, world!")

