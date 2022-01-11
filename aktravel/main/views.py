from django.shortcuts import render
from django.http import HttpResponse
from .models import Oferta, Ksiazki

# Create your views here.

def oferta(response, id):
    oferta = Oferta.objects.get(id=id)
    return render(response, "main/oferta.html", {"oferta":oferta})

def home(response):
    oferty = Oferta.objects.all()
    ksiazki = Ksiazki.objects.all()
    loop = Oferta.objects.all()[:int(len(Oferta.objects.all())/3)]
    loop_ksiazki = Ksiazki.objects.all()[:int(len(Ksiazki.objects.all()))]
    length = len(oferty)
    oferty_lista = list(reversed(Oferta.objects.all()))
    return render(response, "main/home.html", {"oferty":oferty, "ksiazki":ksiazki, "class":"col-md-12", "active":"active", "loop":loop, "loop_ksiazki":loop_ksiazki, "oferty_lista":oferty_lista, "length":length})
    
def firma(response):
    return render(response, "main/aktravel.html")

def covid(response):
    return render(response, "main/covid.html")
    
def oferty(response):
    oferty = Oferta.objects.all()
    return render(response, "main/oferty.html", {"oferty":oferty})

def ksiazki(response):
    return render(response, "main/ksiazki.html")
    



