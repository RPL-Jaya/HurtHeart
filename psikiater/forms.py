
from django.forms import ModelForm
from .models import *

class JadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = ("tanggal", "jam_mulai", "jam_selesai", "metode", "keterangan", "kuota_total")