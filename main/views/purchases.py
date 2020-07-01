from django.shortcuts import render

from main.models import Purchase


def purchases(request):
    return render(request, 'purchases.html', {'purchases': Purchase.objects.filter(user=request.user)})
