from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
import os
import stripe
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")


class PaymentsPageView(TemplateView):
    template_name = 'payments/payments.html'
    success_url = reverse_lazy('charge')

    # def get_context_data(self, **kwargs): # new
    #     context = super().get_context_data(**kwargs)
    #     # context['key'] = settings.STRIPE_PUBLISHABLE_KEY
    #     context['key'] = os.environ.get("STRIPE_PUBLISHABLE_KEY")
    #     return context


def charge(request): # new
    stripe.api_key = 'sk_test_o7yeASKfKUYcZgquJQkKmlqU00kw0WhdaK'
    if request.method == 'POST':
#       added has_paid attribute to user for later view restriction
        user = request.user
        user.has_paid = True
        user.save()
        email = request.user.email
        token = request.POST['stripeToken']

        customer = stripe.Customer.create(
            card = token,
            email = email
        )


        subscription = stripe.Subscription.create(
        customer=customer.id,
        items=[{'plan': 'plan_GxnJfVSz42Vay6',
        'quantity': 1,
        }],
        )
        # user.refresh_from_db()  # load the profile instance created by the signal
        # user.userprofile.stripe_id = subscription.id #save the subscription id to refrence later so the user can cancell their account or other stuff regarding payments
        # user.userprofile.save()
        # user.save()

        charge = stripe.Charge.create(
            customer=customer.id,
            amount=499,
            currency='usd',
            description='A Django charge',
            # source=token
            # source=customer.card
        )
#

        return render(request, 'payments/charge.html')

