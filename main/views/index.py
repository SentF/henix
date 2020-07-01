from django.shortcuts import render

from main.models import Game, Announcement, Detection


def index(request):
    return render(request, 'index.html', {'games': Game.objects.all(),
                                          'announcements': Announcement.objects.all(),
                                          'detections': Detection.objects.all()})
