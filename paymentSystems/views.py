from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from main.models import Purchase
from paymentSystems.bitgo import Bitgo


def bitcoin_webhook(request):
    for purchase in Purchase.objects.filter(status="Pending"):
        if Bitgo().get_wallet().get_address(purchase.payment.bitcoin.address).balance >= purchase.payment.cost:
            purchase.status = "Paid"
            purchase.save()

    return JsonResponse({})
