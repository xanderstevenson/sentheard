from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

class PaymentsPageView(TemplateView):
    template_name = 'payments/payments.html'
    success_url = reverse_lazy('payments')