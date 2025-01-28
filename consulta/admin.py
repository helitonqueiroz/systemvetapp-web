from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'tutor', 'cliente', 'truncated_motivo', 'comportamento')
    list_filter = ('data', 'comportamento')
    search_fields = ('tutor__nome', 'cliente__nome')
    raw_id_fields = ('tutor', 'cliente')  # Útil para muitos registros

    def truncated_motivo(self, obj):
        return obj.motivo[:50] + "..." if len(obj.motivo) > 50 else obj.motivo
    truncated_motivo.short_description = 'Motivo (resumo)'