from django.urls import path

from .views import *

urlpatterns = [
    path('test/<str:object_id>/', View.as_view(), name='index'),
]