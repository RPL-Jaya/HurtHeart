from django.contrib import admin

from .models import Pasien, Ulasan
from pasien.models import PesananKonsultasi

# Register your models here.

admin.site.register(Pasien)
admin.site.register(Ulasan)
