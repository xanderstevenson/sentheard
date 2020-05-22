from django.urls import path, include
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('payments/', include('payments.urls')),
]