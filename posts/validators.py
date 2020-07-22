from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from posts.models import Photo


# def validate_file_number_photo(self, form):
#         form.instance.author = self.request.user
#         if Photo.objects.count() < 1:
#             return super().form_valid(form)
#         else:
#             raise ValidationError("Too many records mate")



def validate_file_size_photo(value):
    filesize= value.size
    if filesize > 1048576:
        raise ValidationError("The maximum file size that can be uploaded is 1MB")
    else:
        return value

def validate_file_size_text(value):
    filesize= value.size
    if filesize > 1048576:
        raise ValidationError("The maximum file size that can be uploaded is 1MB")
    else:
        return value

def validate_file_size_audio(value):
    filesize= value.size
    if filesize > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value

def validate_file_size_video(value):
    filesize= value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value

