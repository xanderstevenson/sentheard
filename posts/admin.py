from django.contrib import admin
from .models import Photo, Audio, Video, Text

admin.site.register(Photo)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Text)