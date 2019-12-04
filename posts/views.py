from django.shortcuts import render


def add_photos(request):
    return render(request, "post_media/add_photos.html")

def post_stuff(request):
    return render(request, "post.html")