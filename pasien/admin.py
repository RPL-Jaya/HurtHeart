from django.contrib import admin

from .models import Pasien, Ulasan

# Register your models here.

admin.site.register(Pasien)
admin.site.register(Ulasan)