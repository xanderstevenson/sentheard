from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PhotoForm, AudioForm, VideoForm, TextForm
from .models import Photo, Audio, Video, Text



# class GalleryView(ListView):
#     # model = Post
#     template_name = 'post_media/gallery.html'

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

class CreateVideoView(CreateView):
    model = Video
    form_class = AudioForm
    template_name = 'post_media/add_video.html'
    success_url = reverse_lazy('gallery')


class CreateTextView(CreateView):
    model = Text
    form_class = TextForm
    template_name = 'post_media/add_text.html'
    success_url = reverse_lazy('gallery')


# class HomePageView(ListView):
#     model = Post
#     template_name = 'post_media/gallery.html'


def gallery(request):
    return render(request, "post_media/gallery.html")
# def add_audio(request):
#     return render(request, "post_media/add_audio.html")
# def add_video(request):
#     return render(request, "post_media/add_video.html")
# def text(request):
#     return render(request, "post_media/add_text.html")
def post_stuff(request):
    return render(request, "memories.html")