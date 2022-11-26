from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.

def gameList(request):

    if 'q' in request.GET:
        q = request.GET['q']
        games = Game.objects.filter(name__icontains=q)

    else:
        games = Game.objects.all()

    context = {
        'games': games,
    }
    
    return render(request, 'main.html', context)

class GameDetailView(DetailView):
    model = Game
    template_name = 'game.html'