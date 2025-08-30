from django.urls import path
from . import views

app_name = 'postulaciones'

urlpatterns = [
    path('', views.lista_postulaciones, name='lista'),
    path('<int:pk>/', views.detalle_postulacion, name='detalle'),
    path('crear/', views.crear_postulacion, name='crear'),
    path('<int:pk>/editar/', views.editar_postulacion, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_postulacion, name='eliminar'),
]
