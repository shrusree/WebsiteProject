from django.contrib import admin
from django.urls import path
from posts import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("services", views.services, name="services"),
    path("contacts", views.contacts, name="contacts"),
    path("user", views.user, name="user"),
    path("upload", views.upload, name="upload"),
    path("details", views.details, name="details"),
    path("lists", views.lists, name="lists"),
    path("lists/<int:pk>/", views.delete_cloth, name="delete_cloth"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
