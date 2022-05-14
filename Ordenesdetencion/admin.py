from django.contrib import admin

from Ordenesdetencion.models import Actividad, Comuna, Delito, EstadoCivil, MedidaCautelar, Orden, Pais, Persona, Region, Sexo, Tribunal


admin.site.register(Actividad)
admin.site.register(Comuna)
admin.site.register(Delito)
admin.site.register(EstadoCivil)
admin.site.register(MedidaCautelar)
admin.site.register(Pais)
admin.site.register(Persona)
admin.site.register(Region)
admin.site.register(Sexo)
admin.site.register(Tribunal)
admin.site.register(Orden)