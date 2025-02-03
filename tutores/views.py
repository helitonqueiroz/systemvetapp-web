# tutores/views.py

from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tutor
from .forms import TutorForm
from django.core.paginator import Paginator
import logging

logger = logging.getLogger(__name__)


class DeletarTutorView(LoginRequiredMixin, DeleteView):
    model = Tutor
    template_name = 'tutores/confirmar_exclusao.html'  # Template para confirmação
    success_url = reverse_lazy('tutores:listatutores')  # Redireciona após a exclusão
    context_object_name = 'tutor'

@login_required
def lista_tutores(request):
    """
    View para listar todos os tutores com paginação.
    """
    # Obtém todos os tutores ordenados pelo nome
    tutores = Tutor.objects.all().order_by('nome')
    # Configura a paginação (10 itens por página)
    paginator = Paginator(tutores, 10)
    page_number = request.GET.get('page')  # Obtém o número da página da URL
    page_obj = paginator.get_page(page_number)  # Obtém a página atual
    # Renderiza o template com o contexto
    return render(request, 'tutores/tutores.html', {'tutores': page_obj})
    
@login_required        
def editar_tutor(request, pk):
    """
    View para editar um tutor existente.
    """
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutor atualizado com sucesso!')
            return redirect('tutores:listatutores')
        else:
            messages.error(request, 'Erro ao atualizar o tutor. Verifique os campos.')
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'tutores/editar_tutores.html', {'form': form, 'tutor': tutor})
    
class AdicionarTutorView(LoginRequiredMixin, CreateView):
    """
    View para adicionar um novo tutor.
    """
    model = Tutor
    template_name = 'tutores/adicionar_tutor.html'
    fields = [
        'nome', 'endereco', 'cidade', 'estado', 'cep', 
        'cpf', 'rg', 'telefone', 'email', 'data_nascimento'
    ]
    success_url = reverse_lazy('tutores:listatutores')

    def form_valid(self, form):
        """
        Salva o formulário e exibe uma mensagem de sucesso.
        """
        messages.success(self.request, 'Tutor adicionado com sucesso!')
        print("Formulário válido. Salvando tutor...")  # Log para depuração
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Exibe mensagens de erro se o formulário for inválido.
        """
        print("Formulário inválido:", form.errors)  # Log para depuração
        messages.error(self.request, 'Erro ao adicionar o tutor. Verifique os campos.')
        return super().form_invalid(form)
    
@login_required
def deletar_tutor(request):
    """
    View para excluir um tutor.
    """
    if request.method == 'POST':
        tutor_id = request.POST.get('tutor_id')
        if not tutor_id:
            messages.error(request, 'ID do tutor não fornecido.')
            return JsonResponse({'status': 'error', 'message': 'ID do tutor não fornecido.'}, status=400)
        try:
            tutor = get_object_or_404(Tutor, id=tutor_id)
            tutor.delete()
            messages.success(request, 'Tutor excluído com sucesso!')
            return HttpResponseRedirect(reverse('tutores:listatutores'))  # Redireciona para a lista de tutores
        except Exception as e:
            messages.error(request, f'Erro ao excluir o tutor: {str(e)}')
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        messages.error(request, 'Método não permitido.')
        return JsonResponse({'status': 'error', 'message': 'Método não permitido.'}, status=405)