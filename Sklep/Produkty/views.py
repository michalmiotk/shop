from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Produkty

def index(request):
    zapytanie = Produkty.objects.all()

    return HttpResponse(zapytanie)