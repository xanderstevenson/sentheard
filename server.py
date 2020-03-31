# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys

import stripe
import json
import os

# from flask import Flask, render_template, jsonify, request, send_from_directory
# from dotenv import load_dotenv, find_dotenv


stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

session = stripe.checkout.Session.create(
  payment_method_types=['card'],
  mode='setup',
  setup_intent_data={
    'metadata': {
      'subscription_id': 'prod_GxnG6LPhMbHjYh',
    },
  },
  success_url='https://sentheard.com/success?session_id={CHECKOUT_SESSION_ID}',
  cancel_url='https://sentheard.com/cancel',
)




# stripe.PaymentIntent.create(
#   amount=1000,
#   currency='usd',
#   payment_method_types=['card'],
#   receipt_email='jenny.rosen@example.com',
# )




# This creates a new Customer and attaches the default PaymentMethod in one API call.
# customer = stripe.Customer.create(
#   payment_method=intent.payment_method,
#   email='jenny.rosen@example.com',
#   invoice_settings={
#     'default_payment_method': intent.payment_method,
#   },
# )

# session = stripe.checkout.Session.create(
#   payment_method_types=['card'],
#   mode='setup',
#   setup_intent_data={
#     'metadata': {
#       'subscription_id': 'SUBSCRIPTION_PLAN_ID',
#     },
#   },
#   success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
#   cancel_url='https://example.com/cancel',
# )

# subscription = stripe.Subscription.create(
#     customer=customer.id,
#     items=[
#         {
#             "plan": os.getenv("SUBSCRIPTION_PLAN_ID"),
#         },
#     ],
#     expand=["latest_invoice.payment_intent"]
# )