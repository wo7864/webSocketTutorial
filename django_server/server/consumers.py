import json
import time
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connect')
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):

        # 정보 읽기
        text_data_json = json.loads(text_data)
        print(text_data_json['message'])

        # 메시지 보내기
        for i in range(10):
            self.send(text_data=json.dumps({
                'message': 'response',
                'num':i
            }))
            time.sleep(0.1)