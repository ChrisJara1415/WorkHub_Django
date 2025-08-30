from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Usuario # O el nombre correcto del modelo

admin.site.register(Usuario)