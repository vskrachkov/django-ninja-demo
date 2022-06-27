import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

http = get_asgi_application()

from devices.consumers import WebSocketConsumer

application = ProtocolTypeRouter(
    {
        "http": http,
        "websocket": URLRouter(
            [
                path("ws", WebSocketConsumer.as_asgi()),
            ]
        ),
    }
)
