from django.db import models
from usuarios.models import Usuario

class Reporte(models.Model):
    TIPO_CHOICES = [
        ('Petición', 'Petición'),
        ('Queja', 'Queja'),
        ('Reclamo', 'Reclamo'),
        ('Sugerencia', 'Sugerencia'),
        ('Consulta', 'Consulta'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]
    
    ESTADO_CHOICES = [
        ('Abierto', 'Abierto'),
        ('Cerrado', 'Cerrado'),
        ('En proceso', 'En proceso'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reportes')
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='Abierto')
    descripcion = models.TextField(max_length=300)
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        return self.titulo

class Solucion(models.Model):
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, related_name='soluciones')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    solucion = models.TextField(max_length=300)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Solución'
        verbose_name_plural = 'Soluciones'

    def __str__(self):
        return f"Solución para: {self.reporte.titulo}"
