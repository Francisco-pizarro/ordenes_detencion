from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

from Ordenesdetencion.models import Actividad, Comuna, Delito, EstadoCivil, MedidaCautelar, Orden, Pais, Persona, Region, Sexo, Tribunal

admin.site.register(Actividad)
admin.site.register(Comuna)
admin.site.register(Delito)
admin.site.register(EstadoCivil)
admin.site.register(MedidaCautelar)
admin.site.register(Orden)
admin.site.register(Pais)
admin.site.register(Persona)
admin.site.register(Region)
admin.site.register(Sexo)
admin.site.register(Tribunal)

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name','last_name' )}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name', 'last_name','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Usuario, UsuarioAdmin)