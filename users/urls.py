from django.urls import path, include
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    # path('', include('payments.urls')),
    # path('payments/', auth_views.login, name='payments'),

    path('payments/', include('payments.urls')),
]