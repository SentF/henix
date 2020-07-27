from django.urls import path

from paymentSystems.views import bitcoin_webhook

urlpatterns = [
    path('bitcoin/webhook', bitcoin_webhook),
]