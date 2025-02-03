# systemvet_atendimento/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views
from .views import home, login_view, register_view, custom_logout 

urlpatterns = [
    # Rotas principais
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', custom_logout, name='logout'),  # Rota para logout

    # Apps
    path('clientes/', include('clientes.urls', namespace='clientes')),  # Rotas do app 'clientes'
    path('tutores/', include('tutores.urls', namespace='tutores')),      # Rotas tradicionais do app 'tutores'

    # Admin
    path('admin/', admin.site.urls),

    # # API RESTful
    # path('api/tutores/', include('tutores.urls', namespace='tutores_api')),  # Rotas da API RESTful
    
    # # JWT Authentication
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Adiciona rotas para arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug Toolbar (remover depois)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]