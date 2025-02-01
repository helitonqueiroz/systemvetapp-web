from django.urls import path
from . import views

app_name = 'tutores'  # Namespace da aplicação

urlpatterns = [
    # Rota para listar os tutores (agora usando a função lista_tutores)
    path('', views.lista_tutores, name='listatutores'),

    # Rotas para outras funcionalidades
    path('editar_tutor/<int:pk>/', views.EditarTutor.as_view(), name='editartutores'),
    path('adicionar_tutor/', views.AdicionarTutor.as_view(), name='adicionartutor'),
    path('deletar_tutor/<int:pk>/', views.deletar_tutor, name='deletartutor'),
]