# tutores/urls.py

from django.urls import path
from . import views

app_name = 'tutores'  # Namespace da aplicação

urlpatterns = [
    path('', views.ListaTutores.as_view(), name='listatutores'),
    path('editar_tutor/<int:pk>/', views.EditarTutor.as_view(), name='editartutores'),
    path('adicionar_tutor/', views.AdicionarTutor.as_view(), name='adicionartutor'),
    path('deletar_tutor/<int:pk>/', views.DeletarTutor.as_view(), name='deletartutor'),
]