from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Vacina(models.Model):
    # Constantes para escolhas
    TIPO_VIRAL = 'V'
    TIPO_BACTERIANA = 'B'
    TIPO_POLIVALENTE = 'P'
    TIPO_VIRUS_VIVO = 'VV'
    TIPO_INATIVADA = 'I'

    TIPO_CHOICE = [
        (TIPO_VIRAL, 'Viral'),
        (TIPO_BACTERIANA, 'Bacteriana'),
        (TIPO_POLIVALENTE, 'Polivalente'),
        (TIPO_VIRUS_VIVO, 'Vírus Vivo'),
        (TIPO_INATIVADA, 'Inativada'),
    ]

    # Campos do modelo
    nome = models.CharField(max_length=100, verbose_name="Nome da Vacina")
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICE, verbose_name="Tipo de Vacina")
    fabricante = models.CharField(max_length=50, verbose_name="Fabricante")
    lote = models.CharField(max_length=20, verbose_name="Número do Lote", blank=True, null=True)
    data_validade = models.DateField(verbose_name="Data de Validade", blank=True, null=True)
    doses_necessarias = models.PositiveIntegerField(verbose_name="Doses Necessárias", default=1)
    intervalo_doses = models.PositiveIntegerField(verbose_name="Intervalo entre Doses (dias)", default=30)
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.nome

    def clean(self):
        """
        Validação personalizada para garantir que a data de validade seja futura.
        """
        if self.data_validade and self.data_validade < timezone.now().date():
            raise ValidationError({'data_validade': 'A data de validade não pode ser no passado.'})

    class Meta:
        verbose_name = "Vacina"
        verbose_name_plural = "Vacinas"
        ordering = ['nome']  # Ordena as vacinas por nome por padrão