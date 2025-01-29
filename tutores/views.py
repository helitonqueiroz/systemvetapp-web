from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from .models import Tutor

class ListaTutores(ListView):
    model = Tutor
    template_name = 'tutores/tutores.html'
    context_object_name = 'tutores'

class EditarTutor(UpdateView):
    model = Tutor
    template_name = 'tutores/editar_tutores.html'
    fields = ['nome', 'endereco', 'cidade', 'estado', 'cep', 'cpf', 'rg', 'telefone', 'email', 'data_nascimento']
    success_url = reverse_lazy('tutores:listatutores')  # Redireciona para a lista de tutores após a edição
    context_object_name = 'tutor'