from django import forms
from .models import Tutor

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = [
            'nome', 'endereco', 'cidade', 'estado', 'cep', 'cpf', 'rg',
            'telefone', 'email', 'data_nascimento'
        ]