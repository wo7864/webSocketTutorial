"""
ASGI config for django_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""


import os

from channels.auth import AuthMiddlewareStack  # 추가
from channels.routing import ProtocolTypeRouter, URLRouter  # URLRouter 추가
import server.routing  # chat import
from django.core.asgi import get_asgi_application
from django.conf.urls import url
import django_eventstream
from django_simple_task import django_simple_task_middlware


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = ProtocolTypeRouter(
    {
        "http": URLRouter(
            [
                url(
                    r"^events/(?P<obj_id>\w+)/",
                    AuthMiddlewareStack(
                        URLRouter(django_eventstream.routing.urlpatterns)
                    ),
                    {"format-channels": ["object-{obj_id}"]},
                ),
                url(r"", get_asgi_application()),
            ]
        ),
        "websocket": AuthMiddlewareStack(  # 추가
            URLRouter(server.routing.websocket_urlpatterns)
        ),
    }
)

application = django_simple_task_middlware(application)