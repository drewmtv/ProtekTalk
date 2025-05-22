from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_chat, name='process_chat'),
]