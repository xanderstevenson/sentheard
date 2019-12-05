from django import forms
from .models import Photo, Audio, Video, Text

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'photo',)

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('title', 'audio')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video')

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('title', 'text',)