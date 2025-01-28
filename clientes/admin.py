from django.contrib import admin
from .models import Clientes

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'raca', 'idade', 'genero', 'peso', 'data_nascimento', 'data_cadastro', 'data_atualizacao', 'tutor')
    list_filter = ('tipo', 'genero', 'data_cadastro', 'data_atualizacao')
    search_fields = ('nome', 'raca', 'tutor__nome')
    date_hierarchy = 'data_cadastro'

admin.site.register(Clientes, ClienteAdmin)
