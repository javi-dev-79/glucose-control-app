from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("uno/", views.uno, name="uno"),
    path("dos/", views.dos, name="dos"),
    path("tres/", views.tres, name="tres"),
]
