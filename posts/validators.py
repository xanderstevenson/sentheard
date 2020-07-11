from django.core.exceptions import ValidationError

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

