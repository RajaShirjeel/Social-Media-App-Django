import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            await self.close()
        else:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()
            
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        receiver_channel_name = data.get('receiver_channel_name')

        if receiver_channel_name:
            await self.channel_layer.send(
                receiver_channel_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender_channel_name': self.channel_name,
                }
            )
        else:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender_channel_name': self.channel_name,
                }
            )

    async def chat_message(self, event):
        message = event['message']
        sender_channel_name = event['sender_channel_name']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_channel_name': sender_channel_name
        }))
