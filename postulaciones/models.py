from django.db import models
from usuarios.models import Usuario
from ofertas.models import Oferta

class Postulacion(models.Model):
    ESTADO_CHOICES = [
        ('Aceptada', 'Aceptada'),
        ('Pendiente', 'Pendiente'),
        ('Rechazada', 'Rechazada'),
    ]

    servicio = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='postulaciones')
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='postulaciones')
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Pendiente')

    class Meta:
        verbose_name = 'Postulación'
        verbose_name_plural = 'Postulaciones'
        unique_together = ['servicio', 'empleado']

    def __str__(self):
        return f"{self.empleado.nombres} - {self.servicio.nombre_servicio}"
