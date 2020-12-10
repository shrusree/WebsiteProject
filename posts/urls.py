from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("services", views.services, name="services"),
    path("contacts", views.contacts, name="contacts"),
    path("user", views.user, name="user"),
]
