from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
import uuid
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
# from django.conf import settings



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
    description = models.TextField(max_length=200, default='', null=False)
    photo = models.ImageField(upload_to = 'photos/')
    def __str__(self):
        return self.title



class Audio(models.Model):
    audio_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    # author = models.CharField(default="", max_length=55, null=False)
    title = models.CharField(default="", max_length=20)
    audio = models.FileField(upload_to='audio/')
    def __str__(self):
        return self.title



class Video(models.Model):
    video_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    # author = models.CharField(default="", max_length=55, null=False)
    title = models.CharField(default="", max_length=20)
    video = models.FileField(upload_to='video/')
    def __str__(self):
        return self.title


class Text(models.Model):
    text_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    # author = models.CharField(default="", max_length=55, null=False)
    title = models.CharField(default="", max_length=20)
    text_upload = models.FileField(upload_to='text/', default="")
    def __str__(self):
        return self.title
