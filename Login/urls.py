from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Incluye todas las URLs de la app 'core' en la raíz.
    # Esto hace que la vista de login sea la página principal.
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]