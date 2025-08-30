from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Contrato # O el nombre correcto del modelo

admin.site.register(Contrato)