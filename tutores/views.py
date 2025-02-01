from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Tutor
from django.core.paginator import Paginator
from django.shortcuts import render

def lista_tutores(request):
    # Obtém todos os tutores ordenados pelo nome
    tutores = Tutor.objects.all().order_by('nome')

    # Configura a paginação
    paginator = Paginator(tutores, 10)  # 10 itens por página
    page_number = request.GET.get('page')  # Obtém o número da página da URL
    page_obj = paginator.get_page(page_number)  # Obtém a página atual

    # Renderiza o template com o contexto
    return render(request, 'tutores/tutores.html', {'tutores': page_obj})
        
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

@require_POST
def deletar_tutor(request, pk):
    try:
        tutor = Tutor.objects.get(id=pk)
        tutor.delete()
        return JsonResponse({'status': 'success'})
    except Tutor.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Tutor não encontrado'}, status=404)