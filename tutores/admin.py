from django.contrib import admin
from .models import Tutor
from django import forms
from clientes.models import Clientes

class ClientesInline(admin.TabularInline):
    model = Clientes
    extra = 0

class TutorAdminForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'

    class Media:
        js = ('js/format_fields.js',)

class TutorAdmin(admin.ModelAdmin):
    form = TutorAdminForm
    inlines = [ClientesInline]  # Add the inline form
    

admin.site.register(Tutor, TutorAdmin)

