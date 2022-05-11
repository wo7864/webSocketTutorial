import asyncio
import multiprocessing
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
from django_simple_task import defer

from django_eventstream import send_event

def func(object_id, send):
    while 1:
        print('hi')
        send()
        time.sleep(1)

def send(x):
    print('hi')
    print(x)
    send_event(f'object-tt', 'message', {'text': 'hello world'})
def task1():
    time.sleep(1)
    print("task1 done")

async def task2():
    await asyncio.sleep(1)
    print("task2 done")
class View(APIView):
    # 조회
    def get(self, request, object_id):
        defer(task1)
        defer(task2)
        send_event(f'object-tt', 'message', {'text': 'hello world'})
        defer(send)
        return Response({"data":"test"}, status=200)
