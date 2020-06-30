from django.shortcuts import render

from main.models import Game


def game(request):
    return render(request, 'game.html', {'games': Game.objects.all()[:3]})
