from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
import uuid
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .validators import validate_file_size_photo, validate_file_size_audio, validate_file_size_video, validate_file_size_text
import datetime


# django-storages and boto3
class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

User = get_user_model()

class Photo(models.Model):
    photo_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    # author = models.CharField(default="", max_length=55, null=False)
    title = models.CharField(default="", max_length=20, null=False)
    date = models.DateField(("Date"), auto_now_add=True)
    photo = models.ImageField(upload_to = 'photos/', validators=[validate_file_size_photo])
    def __str__(self):
        return self.title



class Audio(models.Model):
    audio_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    # author = models.CharField(default="", max_length=55, null=False)
    title = models.CharField(default="", max_length=20)
    date = models.DateField(("Date"), auto_now_add=True)
    audio = models.FileField(upload_to='audio/', validators=[validate_file_size_audio])
    def __str__(self):
        return self.title



class Video(models.Model):
    video_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    # author = models.CharField(default="", max_length=55, null=False)
    title = models.CharField(default="", max_length=20)
    date = models.DateField(("Date"), auto_now_add=True)
    video = models.FileField(upload_to='video/', validators=[validate_file_size_video])
    def __str__(self):
        return self.title


class Text(models.Model):
    text_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    # author = models.CharField(default="", max_length=55, null=False)
    title = models.CharField(default="", max_length=20)
    date = models.DateField(("Date"), auto_now=True)
    text = models.FileField(upload_to='text/', validators=[validate_file_size_text])
    def __str__(self):
        return self.title
