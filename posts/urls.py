
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
from .views import CreatePhotoView, CreateAudioView, CreateVideoView, CreateTextView


urlpatterns = [

    path('add_photos/', CreatePhotoView.as_view(), name='add_photos'),
    path('add_audio/', CreateAudioView.as_view(), name='add_audio'),
    # path('add_audio/', views.add_audio, name="add_audio"),
    path('add_video/', CreateVideoView.as_view(), name='add_video'),
    # path('add_video/', views.add_video, name="add_video"),
    path('text/', CreateTextView.as_view(), name='text'),
    # path('text/', views.text, name="text"),
    # path('gallery/', GalleryView.as_view(), name='gallery'),
    path('gallery/', views.gallery, name="gallery"),
    path('', views.post_stuff, name="post_stuff"),

]
    # path('post_stuff/add_photos/', views.add_photos, name="add_photos"),