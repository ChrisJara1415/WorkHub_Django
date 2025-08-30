from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Oferta
from .forms import OfertaForm

def lista_ofertas(request):
    ofertas = Oferta.objects.all()
    return render(request, 'ofertas/lista.html', {'ofertas': ofertas})

def detalle_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    return render(request, 'ofertas/detalle.html', {'oferta': oferta})

def crear_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oferta creada exitosamente.')
            return redirect('ofertas:lista')
    else:
        form = OfertaForm()
    return render(request, 'ofertas/crear.html', {'form': form})

def editar_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    if request.method == 'POST':
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oferta actualizada exitosamente.')
            return redirect('ofertas:detalle', pk=oferta.pk)
    else:
        form = OfertaForm(instance=oferta)
    return render(request, 'ofertas/editar.html', {'form': form, 'oferta': oferta})

def eliminar_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    if request.method == 'POST':
        oferta.delete()
        messages.success(request, 'Oferta eliminada exitosamente.')
        return redirect('ofertas:lista')
    return render(request, 'ofertas/eliminar.html', {'oferta': oferta})
