from django.shortcuts import render


def purchases(request):
    return render(request, 'purchases.html')
