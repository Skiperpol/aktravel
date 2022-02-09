from django.db import models

class Oferta(models.Model):
    name = models.CharField(max_length=200)
    opis = models.CharField(max_length=200)
    zdjecie_glowne = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
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
