
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
from .views import CreatePhotoView


urlpatterns = [

    path('add_photos/', CreatePhotoView.as_view(), name='add_photos'),
    path('add_audio/', views.add_audio, name="add_audio"),
    path('add_video/', views.add_video, name="add_video"),
    path('add_text/', views.add_text, name="add_text"),
    path('', views.post_stuff, name="post_stuff"),

]
    # path('post_stuff/add_photos/', views.add_photos, name="add_photos"),