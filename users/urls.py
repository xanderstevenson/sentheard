from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    # path('', include('payments.urls')),
    path('payments/', include('payments.urls')),
]