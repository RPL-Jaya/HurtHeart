from django.forms import ModelForm
from .models import Ulasan, Pembayaran, PesananKonsultasi
from django import forms

class UlasanForm(ModelForm):
    class Meta:
        model = Ulasan
        fields = ('pasien', 'psikiater', 'komentar', 'rating', 'tanggalKonsultasi', 'namaPsikiater')

class PembayaranForm(ModelForm):
    byte_image = forms.FileField()
    class Meta:
        model = Pembayaran
        fields = ['metodePembayaran']

class PesananForm(forms.ModelForm):
    class Meta:
        model = PesananKonsultasi
        fields = ['jadwal_konsultasi']
        # Add the 'psikiater' field
        widgets = {
            'psikiater': forms.Select(),
        }
