from django import forms
from .models import Photo, Audio, Video, Text
from django.contrib.auth import get_user_model


User = get_user_model()

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['author']
        # author = User
        fields = ('title', 'photo')

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        exclude = ['author']
        # author = User
        fields = ('title', 'audio')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ['author']
        fields = ('title', 'video')

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        exclude = ['author']
        fields = ('title', 'text')

