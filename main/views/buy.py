from datetime import datetime
from django.shortcuts import redirect

from paymentSystems.bitgo import *
from paymentSystems.models import *


def buy(request, cheat):
    keys = Key.objects.filter(cheat__id=cheat, purchase=None, duration=int(request.GET.get('duration')))
    if len(keys) < int(request.GET.get('quantity')):
        return redirect(f'/cheats/{cheat}/?error=OutOfStock')


    method = request.GET.get('method')

    purchase = Purchase(user=request.user, date=datetime.now(), payment_method=method, status="Pending")
    purchase.save()

    for _ in range(int(request.GET.get('quantity'))):
        purchase.key_set.add(Key.objects.filter(purchase=None, duration=int(request.GET.get('duration'))).first())

    if method == "Bitcoin":
        bitgo = Bitgo()
        wallet = bitgo.get_wallet()
        address = wallet.create_address()

        payment = Payment(purchase=purchase)
        payment.save()

        purchase.payment.bitcoin = BitcoinPayment(address=address)

        bitcoin = BitcoinPayment(address=address)
        bitcoin.save()

        payment.bitcoin = bitcoin
        payment.save()
        purchase.save()



    return redirect(f'/purchases/?open={purchase.id}')