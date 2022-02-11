from django.db import models

class Oferta(models.Model):
    tytul = models.TextField(max_length=200)
    historia = models.TextField(max_length=400, null=True, blank=True)
    opis_dni = models.TextField(max_length=10000, null=True, blank=True)
    termin = models.TextField(max_length=50, null=True, blank=True)
    cena = models.CharField(max_length=50, null=True, blank=True)
    cena_zawiera = models.TextField(max_length=1000, null=True, blank=True)
    cena_nie_zawiera = models.TextField(max_length=1000, null=True, blank=True)
    wazne_informacje = models.TextField(max_length=1000, null=True, blank=True)
    uwagi = models.TextField(max_length=1000, null=True, blank=True)
    zdjecie_glowne = models.ImageField(null=True, blank=True)
    def str(self):
        return self.tytul
    class Meta: 
        verbose_name = "Oferta"
        verbose_name_plural = "Oferty"

class Ksiazki(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    opis = models.CharField(max_length=2000)
    link = models.CharField(max_length=100)
    zdjecie_glowne = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.tytul
    class Meta: 
        verbose_name = "Ksiażka"
        verbose_name_plural = "Książki"
