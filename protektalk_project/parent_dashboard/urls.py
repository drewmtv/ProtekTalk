from django.urls import path

from . import views

app_name = "parent_dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("contact/", views.contact, name="contact")
]