from django.contrib import admin
from .models import Raza,Estado,Mascota,Genero,Adoptante,GeneroAdoptante,Region,Ciudad,tipoVivienda
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza','genero','imagen','estado')
    search_fields = ['raza']
    list_filter = ('raza',)


admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascota,MascotaAdmin)
admin.site.register(Genero)
admin.site.register(Adoptante)
admin.site.register(GeneroAdoptante)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(tipoVivienda)