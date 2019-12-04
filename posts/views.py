from django.shortcuts import render

def add_photos(request):
    return render(request, "post_media/add_photos.html")
def add_audio(request):
    return render(request, "post_media/add_audio.html")
def add_video(request):
    return render(request, "post_media/add_video.html")
def add_text(request):
    return render(request, "post_media/add_text.html")
def post_stuff(request):
    return render(request, "memories.html")