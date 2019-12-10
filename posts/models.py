from django.db import models
from django_s3_storage.storage import S3Storage
import uuid

# django-storages and boto3
class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
#


storage = S3Storage(aws_s3_bucket_name='django-static-sentheard')


class Photo(models.Model):
    uuid = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(default="", max_length=55)
    photo = models.ImageField(storage=storage, default="")
    def __str__(self):
        return self.title

class Audio(models.Model):
    uuid = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(default="", max_length=55)
    audio = models.FileField(storage=storage, default="")
    def __str__(self):
        return self.title

class Video(models.Model):
    uuid = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(default="", max_length=55)
    video = models.FileField(storage=storage, default="")
    def __str__(self):
        return self.name + ": " + str(self.video)


class Text(models.Model):
    uuid = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(default="", max_length=55)
    text_typed = models.TextField(default="", max_length=510)
    text_upload = models.FileField(storage=storage, default="")
    def __str__(self):
        return self.title


# class Published(models.Model):
#     photos_all = Photo.objects.all()
#     audio_all = Audio.objects.all()
#     video_all = Video.objects.all()
#     text_all = Text.objects.all()


# class Post(models.Model):
#     title = models.TextField()
#     cover = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.title

# class Photo(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False,
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100)
#     photo = models.FileField()

#     def __str__(self):
#         return self.title