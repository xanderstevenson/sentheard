from django.core.management.base import BaseCommand
from blogapp.models import Photo, Audio, Video, Text
class Command(BaseCommand):
    def handle(self, *args, **options):
        Photo.objects.all().delete()
        Audio.objects.all().delete()
        Video.objects.all().delete()
        Text.objects.all().delete()


        #python manage.py clear_models