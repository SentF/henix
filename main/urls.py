from django.urls import path

from main.views.cheat import cheat
from main.views.game import game
from main.views.index import index
from main.views.purchases import purchases

urlpatterns = [
    path('', index, name='index'),
    path('game/', game, name='game'),
    path('cheat/', cheat, name='cheat'),
    path('purchases', purchases, name='purchases'),
]