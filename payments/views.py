from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
import os
import stripe
from django.conf import settings

stripe.api_key = "sk_test_o7yeASKfKUYcZgquJQkKmlqU00kw0WhdaK"


class PaymentsPageView(TemplateView):
    template_name = 'payments/payments.html'
    success_url = reverse_lazy('charge')

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        # context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['key'] = os.environ.get("STRIPE_PUBLISHABLE_KEY")
        return context

def charge(request): # new
    if request.method == 'POST':
#
        user = request.user
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

# class CheckoutPageView(TemplateView):
#     template_name = 'payments/checkout.html'
#     success_url = reverse_lazy('login')