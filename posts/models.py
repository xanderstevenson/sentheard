from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
# from django.conf import settings

# django-storages and boto3
class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
#


# storage = S3Storage(aws_s3_bucket_name='django-static-sentheard')
# User = settings.AUTH_USER_MODEL
User = get_user_model()

class Photo(models.Model):
    photo_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(default="", max_length=55)
    description = models.TextField(max_length=500, default='', null=False)
    photo = models.ImageField(upload_to='photos/', default="")
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse_lazy('posts:photo_gallery', args=[self.id])


class Audio(models.Model):
    audio_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None, null=True)
    title = models.CharField(default="", max_length=55)
    audio = models.FileField(upload_to='audio/', default="")
    def __str__(self):
        return self.title



class Video(models.Model):
    video_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None, null=True)
    title = models.CharField(default="", max_length=55)
    video = models.FileField(upload_to='video/', default="")
    def __str__(self):
        return self.title


class Text(models.Model):
    text_id = models.UUIDField(
    primary_key=False, default=uuid.uuid4, editable=False,)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None, null=True)
    title = models.CharField(default="", max_length=55)
    # text_typed = models.TextField(default="", max_length=510)
    text_upload = models.FileField(upload_to='text/', default="")
    def __str__(self):
        return self.title
