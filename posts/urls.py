
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('post_stuff/', views.post_stuff, name="post_stuff"),
    path('post_stuff/add_photos/', views.add_photos, name="add_photos"),

]