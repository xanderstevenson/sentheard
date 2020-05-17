from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import permission_required, login_required
from .forms import PhotoForm, AudioForm, VideoForm, TextForm
from posts.models import Photo, Audio, Video, Text
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.views import generic
from django.views.generic.edit import FormMixin
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

User = get_user_model()

def post_stuff(request):
    return render(request, "memories.html")


class CreatePhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'post_media/add_photos.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# def audio(request):
#     return render(request, "/post_media/post_audio.html")

class CreateAudioView(CreateView):
    # permission_required = 'users.has_paid'
    model = Audio
    form_class = AudioForm
    template_name = 'post_media/add_audio.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateRecordAudioView(CreateView):
    model = Audio
    form_class = AudioForm
    template_name = 'post_media/record_audio.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateVideoView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'post_media/add_video.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateRecordVideoView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'post_media/record_video.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateTextView(CreateView):
    model = Text
    form_class = TextForm
    template_name = 'post_media/add_text.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class GalleryListView(ListView):
#     template_name = 'post_media/gallery.html'
#     queryset = Photo.objects.all()
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context

def GalleryListView(request):
    return render(request, "post_media/gallery.html")


class PhotoGalleryListView(ListView):
    model = Photo
    template_name = 'post_media/galleries/photo_gallery.html'
    queryset = Photo.objects.all().order_by('photo_id')
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]
    context_object_name = 'photo_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context



class AudioGalleryListView(ListView):
    model = Audio
    template_name = 'post_media/galleries/audio_gallery.html'
    queryset = Audio.objects.all().order_by('audio_id')
    context_object_name = 'audio_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class VideoGalleryListView(ListView):
    model = Video
    template_name = 'post_media/galleries/video_gallery.html'
    context_object_name = 'video_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class TextGalleryListView(ListView):
    model = Text
    template_name = 'post_media/galleries/text_gallery.html'
    context_object_name = 'text_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context






def post_video(request):
    return render(request, "post_media/post_video.html")


