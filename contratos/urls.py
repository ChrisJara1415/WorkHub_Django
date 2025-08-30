from django.urls import path
from . import views

app_name = 'contratos'

urlpatterns = [
    path('', views.lista_contratos, name='lista'),
    path('<int:pk>/', views.detalle_contrato, name='detalle'),
    path('crear/', views.crear_contrato, name='crear'),
    path('<int:pk>/editar/', views.editar_contrato, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_contrato, name='eliminar'),
]
