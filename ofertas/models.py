from django.db import models
from usuarios.models import Usuario

class Oferta(models.Model):
    MUNICIPIOS_CHOICES = [
        ('Barbosa', 'Barbosa'),
        ('Copacabana', 'Copacabana'),
        ('Girardota', 'Girardota'),
        ('Bello', 'Bello'),
        ('Medellín', 'Medellín'),
        ('Envigado', 'Envigado'),
        ('Itagüí', 'Itagüí'),
        ('Sabaneta', 'Sabaneta'),
        ('La Estrella', 'La Estrella'),
        ('Caldas', 'Caldas'),
    ]
    
    CATEGORIA_CHOICES = [
        ('Jardinería', 'Jardinería'),
        ('Limpieza', 'Limpieza'),
        ('Piscinero', 'Piscinero'),
        ('Carpintería', 'Carpintería'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Plomería', 'Plomería'),
    ]

    empleador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ofertas')
    municipio_id = models.IntegerField()
    municipio_nombre = models.CharField(max_length=20, choices=MUNICIPIOS_CHOICES)
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    precio_referencia = models.DecimalField(max_digits=10, decimal_places=2)
    personas_requeridas = models.PositiveIntegerField()
    detalle_requerimiento = models.TextField(max_length=500)
    visible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        return self.nombre_servicio
