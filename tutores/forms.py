# tutores/forms.py

from django import forms
from .models import Tutor

class TutorForm(forms.ModelForm):
    """
    Formulário para o modelo Tutor.
    """
    class Meta:
        model = Tutor
        fields = [
            'nome', 'endereco', 'cidade', 'estado', 'cep',
            'cpf', 'rg', 'telefone', 'email', 'data_nascimento'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
