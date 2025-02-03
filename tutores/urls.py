# tutores/urls.py

from django.urls import path
from .views import (
    lista_tutores,
    editar_tutor,
    AdicionarTutorView,
    DeletarTutorView,
)

app_name = 'tutores'  # Namespace para rotas HTML

urlpatterns = [
    # Rotas tradicionais (HTML)
    path('', lista_tutores, name='listatutores'),
    path('editar_tutor/<int:pk>/', editar_tutor, name='editar_tutor'),
    path('adicionar/', AdicionarTutorView.as_view(), name='adicionartutor'),
    path('deletar/<int:pk>/', DeletarTutorView.as_view(), name='deletar_tutor'),

    # Rotas de APIs RESTful (comentadas)
    # path('api/tutores/', TutorListView.as_view(), name='tutor-list'),
    # path('api/tutores/<int:pk>/', TutorDetailView.as_view(), name='tutor-detail'),
]