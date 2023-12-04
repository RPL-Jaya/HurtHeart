from django.forms import ModelForm
from .models import Ulasan, Pembayaran
from django import forms

class UlasanForm(ModelForm):
    class Meta:
        model = Ulasan
        fields = ('pasien', 'psikiater', 'komentar', 'rating', 'tanggalKonsultasi', 'namaPsikiater')

class PembayaranForm(ModelForm):
    class Meta:
        model = Pembayaran
        exclude = ['pasien', 'biayaPembayaran', 'statusPembayaran']