
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('shop/', views.shop, name="shop"),
    path('donate/', views.donate, name="donate"),
    path('about_us/', views.about_us, name="about_us"),
    path('yourAccount/', views.yourAccount, name="yourAccount"),
    path('post_stuff/', include('posts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

]
