from django.shortcuts import render

from main.models import Game, Cheat


def cheat(request, cheat):
    cheat = Cheat.objects.get(id=cheat)
    return render(request, 'cheat.html', {'games': Game.objects.all()[:3],
                                          'cheat': cheat,
                                          'cheats': Cheat.objects.filter(game=cheat.game).exclude(id=cheat.id)})
