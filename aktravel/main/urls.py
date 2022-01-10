from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.oferta, name="oferta"),
    path("", views.home, name=""),
    path("aktravel/", views.firma, name="firma"),
    path("covid/", views.covid, name="covid"),
    path("oferty/", views.oferty, name="oferty"),
    path("ksiazki/", views.ksiazki, name="ksiazki"),
]