from django import views
from django.contrib import admin
from . import path

urlpatterns = [
    path('playground/hello', views.say_hello),
]
