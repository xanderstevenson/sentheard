from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    # path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', auth_views.PasswordResetComp)
]