from django.shortcuts import render


def cheat(request):
    return render(request, 'cheat.html')
