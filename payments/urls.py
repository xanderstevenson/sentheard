from django.urls import path
from .views import PaymentsPageView
from . import views

urlpatterns = [
    path('', PaymentsPageView.as_view(), name='payments'),
    path('charge/', views.charge, name='charge'),
]