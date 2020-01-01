from django import forms
from .models import Photo, Audio, Video, Text


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'photo', 'author')

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('title', 'audio', 'author')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video', 'author')

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('title', 'text_upload', 'author')

