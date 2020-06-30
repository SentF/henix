from django.urls import path

from main.views.index import index

urlpatterns = [
    path('', index, name='index'),
]