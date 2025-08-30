from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Reporte
from .forms import ReporteForm
from usuarios.models import Usuario
from ofertas.models import Oferta
from postulaciones.models import Postulacion
from contratos.models import Contrato

def dashboard(request):
    # Estadísticas generales
    total_usuarios = Usuario.objects.count()
    total_ofertas = Oferta.objects.count()
    total_postulaciones = Postulacion.objects.count()
    total_contratos = Contrato.objects.count()
    total_reportes = Reporte.objects.count()
    
    # Reportes por estado
    reportes_abiertos = Reporte.objects.filter(estado='Abierto').count()
    reportes_proceso = Reporte.objects.filter(estado='En proceso').count()
    reportes_cerrados = Reporte.objects.filter(estado='Cerrado').count()
    
    # Últimos reportes
    ultimos_reportes = Reporte.objects.order_by('-fecha_reporte')[:5]
    
    context = {
        'total_usuarios': total_usuarios,
        'total_ofertas': total_ofertas,
        'total_postulaciones': total_postulaciones,
        'total_contratos': total_contratos,
        'total_reportes': total_reportes,
        'reportes_abiertos': reportes_abiertos,
        'reportes_proceso': reportes_proceso,
        'reportes_cerrados': reportes_cerrados,
        'ultimos_reportes': ultimos_reportes,
    }
    return render(request, 'dashboard.html', context)

def lista_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'reportes/lista.html', {'reportes': reportes})

def detalle_reporte(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    return render(request, 'reportes/detalle.html', {'reporte': reporte})

def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reporte creado exitosamente.')
            return redirect('reportes:lista')
    else:
        form = ReporteForm()
    return render(request, 'reportes/crear.html', {'form': form})

def editar_reporte(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reporte actualizado exitosamente.')
            return redirect('reportes:detalle', pk=reporte.pk)
    else:
        form = ReporteForm(instance=reporte)
    return render(request, 'reportes/editar.html', {'form': form, 'reporte': reporte})

def eliminar_reporte(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    if request.method == 'POST':
        reporte.delete()
        messages.success(request, 'Reporte eliminado exitosamente.')
        return redirect('reportes:lista')
    return render(request, 'reportes/eliminar.html', {'reporte': reporte})
