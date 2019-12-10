
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
from .views import CreatePhotoView, CreateAudioView, CreateVideoView, CreateTextView, GalleryListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('add_photos/', CreatePhotoView.as_view(), name='add_photos'),
    path('add_audio/', CreateAudioView.as_view(), name='add_audio'),
    # path('add_audio/', views.add_audio, name="add_audio"),
    path('add_video/', CreateVideoView.as_view(), name='add_video'),
    # path('add_video/', views.add_video, name="add_video"),
    path('text/', CreateTextView.as_view(), name='text'),
    # path('published/', PublishedList.as_view(), name='published'),
    path('gallery/', GalleryListView.as_view(), name="gallery"),
    path('', views.post_stuff, name="post_stuff"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path('post_stuff/add_photos/', views.add_photos, name="add_photos"),