from django.db import models
from django.apps import apps
from django.core.exceptions import ValidationError

class Clientes(models.Model):
    TIPO_CHOICES = [
        ('C', 'Canino'),
        ('F', 'Felino'),
        ('B', 'Bovino'),
        ('E', 'Equino'),
        ('A', 'Aves'),
        ('S', 'Silvestres'),
        ('O', 'Outros'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='C')
    raca = models.CharField(max_length=50, blank=True, null=True)
    idade = models.PositiveIntegerField(blank=True, null=True)
    genero = models.CharField(max_length=1, choices=[
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ], blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    tutor = models.ForeignKey('tutores.Tutor', on_delete=models.CASCADE, related_name='pets')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

    def clean(self):
        if self.idade and self.idade < 0:
            raise ValidationError({'idade': "A idade não pode ser negativa."})
        if self.peso and self.peso < 0:
            raise ValidationError({'peso': "O peso não pode ser negativo."})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

