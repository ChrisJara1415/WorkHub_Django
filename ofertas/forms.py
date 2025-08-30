from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__'
        widgets = {
            'empleador': forms.Select(attrs={'class': 'form-control'}),
            'municipio_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'municipio_nombre': forms.Select(attrs={'class': 'form-control'}),
            'nombre_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'precio_referencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'personas_requeridas': forms.NumberInput(attrs={'class': 'form-control'}),
            'detalle_requerimiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_limite': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
