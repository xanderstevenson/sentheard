from django.db import models
from django_s3_storage.storage import S3Storage
import uuid

storage = S3Storage(aws_s3_bucket_name='django-static-sentheard')


class Car(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(storage=storage)



class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Photo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    photo = models.FileField()

    def __str__(self):
        return self.title