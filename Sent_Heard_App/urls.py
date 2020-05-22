
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('shop/', views.shop, name="shop"),
    path('donate/', views.donate, name="donate"),
    path('about_us/', views.about_us, name="about_us"),
    path('account/', views.account, name="account"),
    path('post_stuff/', include('posts.urls')),
    # path('post/', views.post, name="post"),
    # path('password_reset/', views.password_reset, name="password_reset"),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('', views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
]
