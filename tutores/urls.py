# tutores/urls.py

from django.urls import path
from . import views

app_name = 'tutores'  # Namespace da aplicação

urlpatterns = [
    path('', views.lista_tutores, name='listatutores'),
    path('editar_tutor/<int:pk>/', views.editar_tutor, name='editartutores'),
    path('adicionar_tutor/', views.AdicionarTutor.as_view(), name='adicionartutor'),
    path('deletar_tutor/<int:pk>/', views.deletar_tutor, name='deletartutor'),
]