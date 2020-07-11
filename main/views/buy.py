from django.shortcuts import redirect

from main.models import Key, Price


def buy(request, cheat):
    keys = Key.objects.filter(cheat__id=cheat, purchase=None, duration=int(request.GET.get('duration')))
    if len(keys) < int(request.GET.get('quantity')):
        return redirect(f'/cheats/{cheat}/?error=OutOfStock')

    price = Price.objects.get(cheat__id=cheat, duration=int(request.GET.get('duration')))

    print(price.price*int(request.GET.get('quantity')))
    return redirect(f'/cheats/{keys[0].cheat.id}')