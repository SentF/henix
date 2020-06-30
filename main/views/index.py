from django.shortcuts import render

from main.models import Game


def index(request):
    return render(request, 'index.html', {'games': Game.objects.all()})
