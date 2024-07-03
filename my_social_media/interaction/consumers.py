import json
from django.contrib.auth import get_user_model

from channels.generic.websocket import AsyncWebsocketConsumer


User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    pass
