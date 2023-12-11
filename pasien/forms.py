from django.forms import ModelForm
from .models import Ulasan, Pembayaran, PesananKonsultasi
from django import forms
from psikiater.models import JadwalKonsultasi 

class UlasanForm(ModelForm):
    class Meta:
        model = Ulasan
        fields = ('pasien', 'psikiater', 'komentar', 'rating', 'tanggalKonsultasi', 'namaPsikiater')

class PembayaranForm(ModelForm):
    class Meta:
        model = Pembayaran
        exclude = ['pasien', 'biayaPembayaran', 'statusPembayaran']

class PesananForm(ModelForm):
    class Meta:
        model = PesananKonsultasi
        fields = ('jadwal_konsultasi',)