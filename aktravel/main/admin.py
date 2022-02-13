from django.contrib import admin
from .models import Oferta, Ksiazki, Zdjecia

admin.site.site_header = "Aktravel panel administracyjny"

admin.site.index_title = ('Aktravel')
admin.site.site_title = ('Panel administracyjny')
# Register your models here.
admin.site.register(Oferta)
admin.site.register(Ksiazki)
admin.site.register(Zdjecia)