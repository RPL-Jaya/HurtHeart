from django.forms import ModelForm
from .models import Ulasan, PesananKonsultasi
from django import forms
from psikiater.models import JadwalKonsultasi 

class UlasanForm(ModelForm):
    class Meta:
        model = Ulasan
        fields = ('pasien', 'psikiater', 'komentar', 'rating', 'tanggalKonsultasi', 'namaPsikiater')

class PesananKonsultasiForm(forms.ModelForm):
    class Meta:
        model = PesananKonsultasi
        fields = ['pasien', 'jadwal_konsultasi']
    