from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]