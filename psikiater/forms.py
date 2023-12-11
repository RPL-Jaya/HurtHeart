from django import forms
from django.forms import ModelForm
from .models import *

class JadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = ("tanggal", "jam_mulai", "jam_selesai", "metode", "keterangan", "kuota_total")

class JadwalKonsultasiForm(forms.ModelForm):
    class Meta:
        model = JadwalKonsultasi
        fields = ['psikiater','jadwal_konsultasi']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Query all available psikiaters
        self.fields['psikiater'].queryset = Psikiater.objects.all()

        # You can customize the label for the psikiater field if needed
        self.fields['psikiater'].label = 'Nama Psikiater'