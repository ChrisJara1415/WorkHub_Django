from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Reporte # O el nombre correcto del modelo

admin.site.register(Reporte)