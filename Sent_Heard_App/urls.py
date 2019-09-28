
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('about_us/', views.about_us, name="about_us"),
    path('', views.index, name="index"),
]
