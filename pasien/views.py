from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse


from .models import Pasien, Ulasan, PesananKonsultasi
from .forms import UlasanForm

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

@api_view(['GET', 'POST'])
@csrf_exempt
def pesanan_konsultasi_pasien(request):
    if request.method == 'GET':
        pesanan_konsultasi = PesananKonsultasi.objects.all()
        serialized_data = serializers.serialize('json', pesanan_konsultasi)
        return JsonResponse({'pesanan_konsultasi': serialized_data}, safe=False)

    elif request.method == 'POST':
        data = request.data
        pesanan_konsultasi = PesananKonsultasi.objects.create(
            pasien=data['pasien'],
            jadwal_konsultasi_id=data['jadwal_konsultasi_id'],
        )
        serialized_data = serializers.serialize('json', [pesanan_konsultasi])
        return JsonResponse({'pesanan_konsultasi': serialized_data}, safe=False)