from django.urls import path

from main.views.cheat import cheat
from main.views.game import game
from main.views.index import index
from main.views.purchases import purchases

urlpatterns = [
    path('', index, name='index'),
    path('games/<int:game>/', game, name='game'),
    path('cheats/<int:cheat>/', cheat, name='cheat'),
    path('purchases/', purchases, name='purchases'),
]