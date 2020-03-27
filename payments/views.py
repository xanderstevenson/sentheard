from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
import os
import stripe
from django.conf import settings

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")


class PaymentsPageView(TemplateView):
    template_name = 'payments/payments.html'
    success_url = reverse_lazy('checkout')

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=499,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'payments/checkout.html')

class CheckoutPageView(TemplateView):
    template_name = 'payments/checkout.html'
    success_url = reverse_lazy('login')