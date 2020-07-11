
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('stal/', views.stal, name="stal"),
    path('stal', views.stal, name="stal"),
    path('sifu_bach/', views.sifu_bach, name="sifu_bach"),
    path('shop/', views.shop, name="shop"),
    path('donate/', views.donate, name="donate"),
    path('about_us/', views.about_us, name="about_us"),
    path('yourAccount/', views.yourAccount, name="yourAccount"),
    path('delete_user/', views.delete_user, name="delete_user"),
    path('delete_user_confirm/', views.delete_user_confirm, name="delete_user_confirm"),
    path('post_stuff/', include('posts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('/', TemplateView.as_view(template_name='index.html'), name='index'),
]
