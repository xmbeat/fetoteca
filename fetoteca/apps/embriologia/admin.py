from django.contrib import admin

# Register your models here.
from .models import Feto, Malformacion, ImagenFeto


admin.site.register(Feto)
admin.site.register(Malformacion)
admin.site.register(ImagenFeto)