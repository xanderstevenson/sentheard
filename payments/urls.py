from django.urls import path
from .views import PaymentsPageView, CheckoutPageView
from . import views

urlpatterns = [
    path('', PaymentsPageView.as_view(), name='payments'),
    path('checkout/', CheckoutPageView.as_view(), name='checkout'),
]