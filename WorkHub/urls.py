from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('admin/usuarios/', include('usuarios.urls')),
    path('admin/ofertas/', include('ofertas.urls')),
    path('admin/postulaciones/', include('postulaciones.urls')),
    path('admin/contratos/', include('contratos.urls')),
    path('admin/reportes/', include('reportes.urls')),
]
