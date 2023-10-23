from django.contrib import admin
from django.urls import path, include
from rec import views


urlpatterns = [

    path('', views.user)
]
