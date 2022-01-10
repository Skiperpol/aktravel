from django.db import models

class Oferta(models.Model):
    name = models.CharField(max_length=200)
    opis = models.CharField(max_length=200)
    zdjecie_glowne = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
