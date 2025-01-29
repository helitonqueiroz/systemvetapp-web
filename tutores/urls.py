from django.urls import path
from . import views

app_name = 'tutores'

urlpatterns = [
    path('', views.ListaTutores.as_view(), name='listatutores'),
    path('editar_tutor/<int:pk>/', views.EditarTutor.as_view(), name='editartutores'),
]