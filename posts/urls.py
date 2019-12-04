
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
from .views import CreatePhotoView

urlpatterns = [

    path('post_stuff/add_photos/', CreatePhotoView.as_view(), name='add_photos'),
    path('post_stuff/add_audio/', views.add_audio, name="add_audio"),
    path('post_stuff/add_video/', views.add_video, name="add_video"),
    path('post_stuff/add_text/', views.add_text, name="add_text"),
    path('post_stuff/', views.post_stuff, name="post_stuff"),

]
    # path('post_stuff/add_photos/', views.add_photos, name="add_photos"),