
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
from .views import CreatePhotoView, CreateAudioView, CreateVideoView, CreateTextView, GalleryListView, PhotoGalleryListView,\
AudioGalleryListView, VideoGalleryListView, TextGalleryListView, CreateRecordAudioView,  CreateRecordVideoView
from django.conf import settings
from django.conf.urls.static import static
from .models import Photo
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'posts'

urlpatterns = [

    path('add_photos/', CreatePhotoView.as_view(), name='add_photos'),
    path('add_audio/', CreateAudioView.as_view(), name='add_audio'),
    path('record_audio/', CreateRecordAudioView.as_view(), name='record_audio'),
    path('record_video/', CreateRecordVideoView.as_view(), name='record_video'),
    path('post_audio/', views.post_audio, name="post_audio"),
    path('add_video/', CreateVideoView.as_view(), name='add_video'),
    path('post_video/', views.post_video, name="post_video"),
    path('text/', CreateTextView.as_view(), name='text'),
    # path('published/', PublishedList.as_view(), name='published'),
    path('gallery/', views.GalleryListView, name="gallery"),
    path('gallery/photo_gallery', PhotoGalleryListView.as_view(), name="photo_gallery"),
    path('gallery/audio_gallery', AudioGalleryListView.as_view(), name="audio_gallery"),
    path('gallery/video_gallery', VideoGalleryListView.as_view(), name="video_gallery"),
    path('gallery/text_gallery', TextGalleryListView.as_view(), name="text_gallery"),
    path('', views.post_stuff, name="post_stuff"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
    # path('post_stuff/add_photos/', views.add_photos, name="add_photos"),