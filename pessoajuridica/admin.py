from django.contrib import admin
from .models import PessoaJuridica, ContaBancaria

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'endereco_cidade', 'telefone')
    search_fields = ('razao_social', 'cnpj')
    filter_horizontal = ('clientes', 'tutores')  # Interface amigável para ManyToMany

@admin.register(ContaBancaria)
class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'agencia', 'conta_corrente', 'tipo_conta')
    list_filter = ('tipo_conta',)