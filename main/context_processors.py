from main.models import Game


def all_games(request):
    return {'all_games': Game.objects.all()}
