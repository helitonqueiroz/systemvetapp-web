from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
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
    success_url = reverse_lazy('tutores:listatutores')
    
class AdicionarTutor(CreateView):
    model = Tutor
    template_name = 'tutores/adicionar_tutor.html'
    fields = ['nome', 'endereco', 'cidade', 'estado', 'cep', 'cpf', 'rg', 'telefone', 'email', 'data_nascimento']
    success_url = reverse_lazy('tutores:listatutores')

    def form_valid(self, form):
        messages.success(self.request, 'Tutor adicionado com sucesso!')
        return super().form_valid(form)

class DeletarTutor(DeleteView):  # Nova classe para deletar tutores
    model = Tutor
    template_name = 'tutores/deletar_tutor.html'  # Template para confirmar a exclusão
    success_url = reverse_lazy('tutores:listatutores')  # Redireciona para a lista de tutores após a exclusão
    context_object_name = 'tutor'  # Nome do objeto no template