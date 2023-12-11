from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse


from .models import Pasien, Ulasan, PesananKonsultasi
from .forms import UlasanForm, PesananKonsultasiForm

from psikiater.models import Psikiater

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from rest_framework.decorators import api_view

# Create your views here.

def buat_ulasan(request):
    print(request)
    form = UlasanForm()
    print(form)
    if request.method == 'POST':
        form = UlasanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('psikiater:psikiater_detail', username=form.cleaned_data['psikiater'])

    pasien = Pasien.objects.all()
    psikiater = Psikiater.objects.all()
    context = {'form':form, 'pasien':pasien, 'psikiater':psikiater}
    return render(request, 'ulas.html', context)


def buat_ulasan_api(request):
    print(request)
    form = UlasanForm()
    print(form)
    if request.method == 'POST':
        form = UlasanForm(request.POST)
        if form.is_valid():
            form.save()
            # return JsonResponse({'message': 'Ulasan berhasil dibuat'})
            return JsonResponse({'message': 'Ulasan berhasil dibuat'})

    return JsonResponse({'message': 'Ulasan gagal dibuat'})

def pesanan_konsultasi_pasien(request):
    if request.method == 'POST':
        form = PesananKonsultasiForm(request.POST)
        if form.is_valid():
            pesanan_konsultasi = form.save(commit=False)
            # If you have a specific JadwalKonsultasi instance to associate, replace the next line
            # For example, you might want to get the first JadwalKonsultasi in the database
            pesanan_konsultasi.jadwal_konsultasi = JadwalKonsultasi.objects.first()
            pesanan_konsultasi.save()
            return redirect('pasien:pesanan-list-pasien')

    # If it's a GET request or the form is not valid, render the template with the form
    form = PesananKonsultasiForm()
    pesanan_konsultasi = PesananKonsultasi.objects.all()
    return render(request, 'pesanan_konsultasi_pasien.html', {'form': form, 'pesanan_konsultasi': pesanan_konsultasi})