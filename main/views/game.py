from django.shortcuts import render

from main.models import Game


def game(request, game):
    game = Game.objects.get(id=game)
    return render(request, 'game.html', {'games': Game.objects.all().exclude(id=game.id)[:3],
                                         'game': game,
                                         'cheats': game.cheat_set.all()})
