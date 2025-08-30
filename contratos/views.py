from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Contrato
from .forms import ContratoForm

def lista_contratos(request):
    contratos = Contrato.objects.all()
    return render(request, 'contratos/lista.html', {'contratos': contratos})

def detalle_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    return render(request, 'contratos/detalle.html', {'contrato': contrato})

def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contrato creado exitosamente.')
            return redirect('contratos:lista')
    else:
        form = ContratoForm()
    return render(request, 'contratos/crear.html', {'form': form})

def editar_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contrato actualizado exitosamente.')
            return redirect('contratos:detalle', pk=contrato.pk)
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'contratos/editar.html', {'form': form, 'contrato': contrato})

def eliminar_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        contrato.delete()
        messages.success(request, 'Contrato eliminado exitosamente.')
        return redirect('contratos:lista')
    return render(request, 'contratos/eliminar.html', {'contrato': contrato})
