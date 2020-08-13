from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
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
from django.core.exceptions import PermissionDenied
from django.db.models.signals import pre_save
from django.db import models
from django.dispatch import receiver
import os


User = get_user_model()



def post_stuff(request):
    return render(request, "memories.html")


class CreatePhotoView(CreateView):
    @receiver(pre_save)
    def check_limits(sender, **kwargs):
        if User.objects.count() > 8:
            raise PermissionDenied
    model = Photo
    form_class = PhotoForm
    template_name = 'post_media/add_photos.html'
    success_url = reverse_lazy('posts:photo_gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        kwargs['photo_list'] = Photo.objects.order_by('date')
        return super(CreatePhotoView, self).get_context_data(**kwargs)



class CreateAudioView(CreateView):
    @receiver(pre_save)
    def check_limits(sender, **kwargs):
        if User.objects.count() > 30:
            raise PermissionDenied
    model = Audio
    form_class = AudioForm
    template_name = 'post_media/add_audio.html'
    success_url = reverse_lazy('posts:audio_gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        kwargs['audio_list'] = Audio.objects.order_by('date')
        return super(CreateAudioView, self).get_context_data(**kwargs)



# Not Used
class CreateRecordAudioView(CreateView):
    model = Audio
    form_class = AudioForm
    template_name = 'post_media/record_audio.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateVideoView(CreateView):
    @receiver(pre_save)
    def check_limits(sender, **kwargs):
        if User.objects.count() > 30:
            raise PermissionDenied
    model = Video
    form_class = VideoForm
    template_name = 'post_media/add_video.html'
    success_url = reverse_lazy('posts:video_gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# Not Used
class CreateRecordVideoView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'post_media/record_video.html'
    success_url = reverse_lazy('posts:gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateTextView(CreateView):
    @receiver(pre_save)
    def check_limits(sender, **kwargs):
        if User.objects.count() > 30:
            raise PermissionDenied
    model = Text
    form_class = TextForm
    template_name = 'post_media/add_text.html'
    success_url = reverse_lazy('posts:text_gallery')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def GalleryListView(request):
    return render(request, "post_media/gallery.html")


class PhotoGalleryListView(ListView):
    model = Photo
    template_name = 'post_media/galleries/photo_gallery.html'
    queryset = Photo.objects.all().order_by('date')[:10]
    context_object_name = 'photo_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context



class AudioGalleryListView(ListView):
    model = Audio
    template_name = 'post_media/galleries/audio_gallery.html'
    queryset = Audio.objects.all().order_by('date')[:5]
    context_object_name = 'audio_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class VideoGalleryListView(ListView):
    model = Video
    template_name = 'post_media/galleries/video_gallery.html'
    queryset = Video.objects.all().order_by('date')[:5]
    context_object_name = 'video_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class TextGalleryListView(ListView):
    model = Text
    template_name = 'post_media/galleries/text_gallery.html'
    queryset = Text.objects.all().order_by('date')[:10]
    context_object_name = 'text_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

def post_video(request):
    return render(request, "post_media/post_video.html")

class DeletePhotoView(DeleteView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'post_media/delete.html'
    success_url = reverse_lazy('posts:gallery')
    def test_func(self):
      obj = self.get_object()
      if obj.user == self.request.user:
        return True
      return False

    #This code does magic for S3 file deletion
    @receiver(models.signals.pre_delete, sender=Photo)
    def remove_file_from_s3(sender, instance, using, **kwargs):
       instance.photo.delete(save=False)

class DeleteAudioView(DeleteView):
    model = Audio
    context_object_name = 'audio'
    template_name = 'post_media/delete.html'
    success_url = reverse_lazy('posts:gallery')
    def test_func(self):
      obj = self.get_object()
      if obj.user == self.request.user:
        return True
      return False

    #This code does magic for S3 file deletion
    @receiver(models.signals.pre_delete, sender=Audio)
    def remove_file_from_s3(sender, instance, using, **kwargs):
       instance.audio.delete(save=False)

class DeleteTextView(DeleteView):
    model = Text
    context_object_name = 'text'
    template_name = 'post_media/delete.html'
    success_url = reverse_lazy('posts:gallery')
    def test_func(self):
      obj = self.get_object()
      if obj.user == self.request.user:
        return True
      return False

    #This code does magic for S3 file deletion
    @receiver(models.signals.pre_delete, sender=Text)
    def remove_file_from_s3(sender, instance, using, **kwargs):
       instance.text.delete(save=False)


class DeleteVideoView(DeleteView):
    model = Video
    context_object_name = 'video'
    template_name = 'post_media/delete.html'
    success_url = reverse_lazy('posts:gallery')
    def test_func(self):
      obj = self.get_object()
      if obj.user == self.request.user:
        return True
      return False

    #This code does magic for S3 file deletion
    @receiver(models.signals.pre_delete, sender=Video)
    def remove_file_from_s3(sender, instance, using, **kwargs):
       instance.video.delete(save=False)
