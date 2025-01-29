from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView  # Import the index view

urlpatterns = [
    path('', IndexView.as_view(), name='base'),  # Add the index view for systemvet_atendimento project    
    path('', include('clientes.urls')),
    path('tutores', include('tutores.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# remover depois
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
