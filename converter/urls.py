from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brazil", views.brazilian_real, name="index"),
]