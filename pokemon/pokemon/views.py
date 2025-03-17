from django.http import HttpResponse
from django.views.generic import ListView
from .models import DatosPokemon
from django.views import View
from django.shortcuts import render

def index(request):
    # last_pokemon_list = DatosPokemon.objects.order_by("-id"[:50])
    # output = ", ".join([p.Nombre for p in last_pokemon_list])
    return HttpResponse("Hello, world. You're at the pokemon index.")

class DashboardView(View):
    def get(self, request):
        pokemones = DatosPokemon.objects.all()
        return render(request, "dashboard.html", {"pokemones":pokemones})
    
    #ejemplo
class PesoView(View):
    def get(self, request):
        pokemones = DatosPokemon.objects.filter(peso__range = (30, 80))
        return render(request, "peso.html", {"pesopokemon" : pokemones})
        