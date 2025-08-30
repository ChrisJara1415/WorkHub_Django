from django.db import models
from usuarios.models import Usuario
from ofertas.models import Oferta

class Contrato(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='contratos')
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_empleado')
    empleador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_empleador')
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return f"Contrato: {self.oferta.nombre_servicio} - {self.empleado.nombres}"
