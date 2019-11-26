from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")

def donate(request):
    return render(request, "donate.html")

def about_us(request):
    return render(request, "about_us.html")

def account(request):
    return render(request, "account.html")

def password_rese(request):
    return render(request, "password_reset_form.html")
