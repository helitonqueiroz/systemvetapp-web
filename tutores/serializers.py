# serializers.py

import re
from rest_framework import serializers
from tutores.models import Tutor

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = [
            'id',  # ID é incluído automaticamente pelo DRF
            'nome',
            'email',
            'telefone',
            'endereco',
            'cidade',
            'estado',
            'cep',
            'cpf',
            'rg',
            'data_nascimento',
            'data_cadastro',
            'data_atualizacao'
        ]
        read_only_fields = ['data_cadastro', 'data_atualizacao']  # Esses campos não devem ser editados manualmente

    def validate_telefone(self, value):
        """
        Valida o formato do telefone antes de salvar.
        """
        pattern = r'^\(\d{2}\) \d{5}-\d{4}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Telefone deve estar no formato: '(99) 99999-9999'.")
        return value

    def validate_cep(self, value):
        """
        Valida o formato do CEP antes de salvar.
        """
        pattern = r'^\d{5}-\d{3}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("CEP deve estar no formato: '99999-999'.")
        return value

    def validate_cpf(self, value):
        """
        Valida o CPF antes de salvar.
        """
        from validarcpf import validar_cpf  # Importe a função de validação de CPF
        if not validar_cpf(value):
            raise serializers.ValidationError("CPF inválido.")
        return value

    def validate_estado(self, value):
        """
        Valida o estado (deve ter exatamente 2 caracteres).
        """
        if len(value) != 2:
            raise serializers.ValidationError("Estado deve ter 2 caracteres.")
        return value.upper()  # Garante que o estado seja salvo em maiúsculas

    def to_representation(self, instance):
        """
        Personaliza a representação JSON do objeto Tutor.
        """
        representation = super().to_representation(instance)
        # Adiciona uma representação personalizada, se necessário
        representation['idade'] = self.calcular_idade(instance.data_nascimento)
        return representation

    def calcular_idade(self, data_nascimento):
        """
        Calcula a idade com base na data de nascimento.
        """
        from datetime import date
        hoje = date.today()
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        return idade