from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Produkty, Kategoria

def index(request):
    kategorie = Kategoria.objects.all()
    print(kategorie)
    dane = {'kategorie' : kategorie}
    return render(request, 'kategorie.html', dane)

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user)

def produkty(request, id):
    produkt = Produkty.objects.get(pk=id)
    dane = {'produkt' : produkt}
    return render(request, 'produkty_id.html', dane)