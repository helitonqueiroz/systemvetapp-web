from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from tutores.models import Tutor
from tutores.serializers import TutorSerializer

# Views para páginas HTML (frontend tradicional)
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')  # Obtém o parâmetro 'next' ou redireciona para 'home'
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

@login_required
def custom_logout(request):
    """
    View personalizada para realizar o logout.
    Aceita tanto GET quanto POST.
    """
    if request.method in ['GET', 'POST']:
        logout(request)
        return redirect('login')  # Redireciona para a página de login após o logout

@login_required
def register_view(request):
    # Verifica se o usuário é um superusuário
    if not request.user.is_superuser:
        messages.error(request, 'Apenas superusuários podem criar novos usuários.')
        return redirect('home')  # Redireciona para a página inicial

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Verifica se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso. Escolha outro.')
            return redirect('register')  # Redireciona de volta para a página de registro

        # Verifica se as senhas coincidem
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('register')

        # Cria o usuário
        try:
            user = User.objects.create_user(username=username, password=password1)
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('home')  # Redireciona para a página inicial
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao registrar o usuário: {str(e)}')
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout