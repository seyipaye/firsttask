from django import views
from django.urls import path

urlpatterns = [
    path('playground/hello', views.say_hello),
]
