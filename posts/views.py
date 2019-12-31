from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PhotoForm, AudioForm, VideoForm, TextForm
from .models import Photo, Audio, Video, Text

# django-storages and boto3
# def image_upload(request):
#     if request.method == 'POST':
#         image_file = request.FILES['image_file']
#         image_type = request.POST['image_type']
#         if settings.USE_S3:
#             upload = Upload(file=image_file)
#             upload.save()
#             image_url = upload.file.url
#         else:
#             fs = FileSystemStorage()
#             filename = fs.save(image_file.name, image_file)
#             image_url = fs.url(filename)
#         return render(request, 'upload.html', {
#             'image_url': image_url
#         })
#     return render(request, 'post_media/published.html')

# #

class CreatePhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'post_media/add_photos.html'
    success_url = reverse_lazy('gallery')

class CreateAudioView(CreateView):
    model = Audio
    form_class = AudioForm
    template_name = 'post_media/add_audio.html'
    success_url = reverse_lazy('gallery')

class CreateRecordAudioView(CreateView):
    model = Audio
    form_class = AudioForm
    template_name = 'post_media/record_audio.html'
    success_url = reverse_lazy('gallery')

class CreateVideoView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'post_media/add_video.html'
    success_url = reverse_lazy('gallery')


class CreateTextView(CreateView):
    model = Text
    form_class = TextForm
    template_name = 'post_media/add_text.html'
    success_url = reverse_lazy('gallery')


class GalleryListView(ListView):
    model = Photo
    template_name = 'post_media/gallery.html'
    context_object_name = 'photo_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PhotoGalleryListView(ListView):
    model = Photo
    template_name = 'post_media/galleries/photo_gallery.html'
    context_object_name = 'photo_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AudioGalleryListView(ListView):
    model = Audio
    template_name = 'post_media/galleries/audio_gallery.html'
    context_object_name = 'audio_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class VideoGalleryListView(ListView):
    model = Video
    template_name = 'post_media/galleries/video_gallery.html'
    context_object_name = 'video_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TextGalleryListView(ListView):
    model = Text
    template_name = 'post_media/galleries/text_gallery.html'
    context_object_name = 'texto_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def post_stuff(request):
    return render(request, "memories.html")


def post_audio(request):
    return render(request, "post_media/post_audio.html")