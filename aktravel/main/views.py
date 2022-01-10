from django.shortcuts import render
from django.http import HttpResponse
from .models import Oferta

# Create your views here.

def oferta(response, id):
    oferta = Oferta.objects.get(id=id)
    return render(response, "main/oferta.html", {"oferta":oferta})

def home(response):
    oferty = Oferta.objects.all()
    loop = Oferta.objects.all()[:int(len(Oferta.objects.all())/3)]
    length = len(oferty)
    oferty_lista = list(reversed(Oferta.objects.all()))
    return render(response, "main/home.html", {"oferty":oferty, "class":"col-md-12", "active":"active", "loop":loop, "oferty_lista":oferty_lista, "length":length})
    
def firma(response):
    return render(response, "main/base.html")

def covid(response):
    return render(response, "main/base.html")
    
def oferty(response):
    oferty = Oferta.objects.all()
    return render(response, "main/base.html", {"oferty":oferty})

def ksiazki(response):
    return render(response, "main/base.html")
    



