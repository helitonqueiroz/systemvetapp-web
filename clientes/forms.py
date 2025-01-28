from django import forms
from clientes.models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'tipo', 'raca', 'idade', 'peso', 'data_nascimento', 'tutor']