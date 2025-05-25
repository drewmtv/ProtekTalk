from django.urls import path

from . import views

app_name = "protektalk_app"

urlpatterns = [
    path("chat/", views.chat_render, name="chat_render"),
    path("chat/process/", views.process_chat, name="process_chat")
]