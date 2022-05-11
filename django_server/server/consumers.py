import json
import time
from channels.generic.websocket import WebsocketConsumer
import multiprocessing
import time
from asgiref.sync import async_to_sync

def func(p2c, c2p):
    i=0
    while i < 100:
        if not p2c.empty():
            v = p2c.get()
            if v == 'fin':
                c2p.put('fin')
        c2p.put(i)
        time.sleep(1)
        i+=1


class Manager:
    def __init__(self) -> None:
        self.ps = {}
        self.i = 0
        pass

manager = Manager()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        print('conn')

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        if data['type'] == 'start':
            if 'test' in manager.ps:
                p, p2c, c2p = manager.ps['test']
            else:
                p2c = multiprocessing.Queue()
                c2p = multiprocessing.Queue()
                p = multiprocessing.Process(target=func, args=(p2c, c2p))
                manager.ps['test'] = (p, p2c, c2p)
                p.start()

            for i in range(4):
                if not p.is_alive():
                    break
                v = None
                while not c2p.empty() :
                    v = c2p.get()

                if v is not None:
                    self.send(text_data=json.dumps({
                        'message': 'response',
                        'num':v
                    }))
                time.sleep(1)

        # elif data['type'] == 'stop':
        #     p = manager.ps['test']
        #     p.terminate()



