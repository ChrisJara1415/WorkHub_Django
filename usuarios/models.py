from django.db import models
from django.core.validators import RegexValidator
import re

class Usuario(models.Model):
    MUNICIPIOS_CHOICES = [
        ('barbosa', 'Barbosa'),
        ('copacabana', 'Copacabana'),
        ('girardota', 'Girardota'),
        ('bello', 'Bello'),
        ('medellin', 'Medellín'),
        ('envigado', 'Envigado'),
        ('itagui', 'Itagüí'),
        ('sabaneta', 'Sabaneta'),
        ('la_estrella', 'La Estrella'),
        ('caldas', 'Caldas'),
    ]
    
    ROL_CHOICES = [
        ('empleado', 'Empleado'),
        ('empleador', 'Empleador'),
    ]
    
    ESTADO_SEGURIDAD_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    nombres = models.CharField(
        max_length=150,
        validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'Solo se permiten letras y espacios')]
    )
    apellidos = models.CharField(
        max_length=150,
        validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'Solo se permiten letras y espacios')]
    )
    email = models.EmailField(unique=True)
    telefono = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(r'^(?:\+57)?3\d{9}$', 'Formato de teléfono inválido')]
    )
    password_hash = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)
    municipio = models.CharField(max_length=20, choices=MUNICIPIOS_CHOICES)
    direccion = models.CharField(
        max_length=255,
        validators=[RegexValidator(r'^[a-zA-Z0-9\s]+$', 'No se permiten caracteres especiales')]
    )
    seguridad_social_nombre = models.CharField(max_length=100)
    seguridad_social_estado = models.CharField(
        max_length=10, 
        choices=ESTADO_SEGURIDAD_CHOICES, 
        default='activo'
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
