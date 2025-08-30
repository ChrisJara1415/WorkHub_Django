from django.urls import path
from . import views

app_name = 'ofertas'

urlpatterns = [
    path('', views.lista_ofertas, name='lista'),
    path('<int:pk>/', views.detalle_oferta, name='detalle'),
    path('crear/', views.crear_oferta, name='crear'),
    path('<int:pk>/editar/', views.editar_oferta, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_oferta, name='eliminar'),
]
