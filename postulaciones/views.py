from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Postulacion
from .forms import PostulacionForm

def lista_postulaciones(request):
    postulaciones = Postulacion.objects.all()
    return render(request, 'postulaciones/lista.html', {'postulaciones': postulaciones})

def detalle_postulacion(request, pk):
    postulacion = get_object_or_404(Postulacion, pk=pk)
    return render(request, 'postulaciones/detalle.html', {'postulacion': postulacion})

def crear_postulacion(request):
    if request.method == 'POST':
        form = PostulacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Postulación creada exitosamente.')
            return redirect('postulaciones:lista')
    else:
        form = PostulacionForm()
    return render(request, 'postulaciones/crear.html', {'form': form})

def editar_postulacion(request, pk):
    postulacion = get_object_or_404(Postulacion, pk=pk)
    if request.method == 'POST':
        form = PostulacionForm(request.POST, instance=postulacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Postulación actualizada exitosamente.')
            return redirect('postulaciones:detalle', pk=postulacion.pk)
    else:
        form = PostulacionForm(instance=postulacion)
    return render(request, 'postulaciones/editar.html', {'form': form, 'postulacion': postulacion})

def eliminar_postulacion(request, pk):
    postulacion = get_object_or_404(Postulacion, pk=pk)
    if request.method == 'POST':
        postulacion.delete()
        messages.success(request, 'Postulación eliminada exitosamente.')
        return redirect('postulaciones:lista')
    return render(request, 'postulaciones/eliminar.html', {'postulacion': postulacion})
