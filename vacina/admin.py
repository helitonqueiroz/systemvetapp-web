from django.contrib import admin
from .models import Vacina

@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'fabricante', 'data_validade')
    search_fields = ('nome', 'fabricante')
    list_filter = ('tipo', 'data_validade')