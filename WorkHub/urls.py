from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('ofertas/', include('ofertas.urls')),
    path('postulaciones/', include('postulaciones.urls')),
    path('contratos/', include('contratos.urls')),
    path('reportes/', include('reportes.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
]
