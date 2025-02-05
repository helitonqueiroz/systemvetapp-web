# tutores/models.py

from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from validarcpf import validar_cpf  # Certifique-se de que esta função está implementada corretamente
import re

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Garante que o email seja único
    telefone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\) \d{5}-\d{4}$',
                message="Telefone deve estar no formato: '(99) 99999-9999'."
            )
        ]
    )
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=2,
        validators=[
            MinLengthValidator(2, message="Estado deve ter 2 caracteres.")
        ]
    )
    cep = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^\d{5}-\d{3}$',
                message="CEP deve estar no formato: '99999-999'."
            )
        ]
    )
    cpf = models.CharField(
        max_length=14,
        unique=True,  # Garante que o CPF seja único
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message="CPF deve estar no formato: '999.999.999-99'."
            )
        ]
    )
    rg = models.CharField(max_length=12)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def clean(self):
        """
        Valida o CPF antes de salvar o modelo.
        """
        if not validar_cpf(self.cpf):
            raise ValidationError({'cpf': "CPF inválido."})

    def save(self, *args, **kwargs):
        """
        Formata os campos antes de salvar o modelo.
        """
        self.telefone = self.formatar_telefone(self.telefone)
        self.cep = self.formatar_cep(self.cep)
        self.cpf = self.formatar_cpf(self.cpf)
        self.clean()  # Executa a validação personalizada
        super().save(*args, **kwargs)

    @staticmethod
    def formatar_telefone(telefone):
        """
        Formata o número de telefone no padrão '(99) 99999-9999'.
        """
        telefone = re.sub(r'\D', '', telefone)
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}" if len(telefone) == 11 else telefone

    @staticmethod
    def formatar_cep(cep):
        """
        Formata o CEP no padrão '99999-999'.
        """
        cep = re.sub(r'\D', '', cep)
        return f"{cep[:5]}-{cep[5:]}" if len(cep) == 8 else cep

    @staticmethod
    def formatar_cpf(cpf):
        """
        Formata o CPF no padrão '999.999.999-99'.
        """
        cpf = re.sub(r'\D', '', cpf)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if len(cpf) == 11 else cpf

    def __str__(self):
        """
        Representação textual do modelo.
        """
        return f"{self.nome} ({self.cpf})"