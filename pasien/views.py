from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Pasien, Ulasan, PesananKonsultasi
from .forms import UlasanForm, PesananForm, PembayaranForm

from psikiater.models import Psikiater, Jadwal
from authentication.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import get_object_or_404


# Create your views here.

def buat_ulasan(request):
    print(request)
    form = UlasanForm()
    print(form)
    if request.method == 'POST':
        form = UlasanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('psikiater:psikiater_detail', username=form.cleaned_data['namaPsikiater'])

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

@login_required(login_url='/login/')
@api_view(['GET', 'POST'])
@csrf_exempt
def pesanan_konsultasi_pasien(request):
    if request.method == 'GET':
        pesanan_konsultasi = PesananKonsultasi.objects.all()
        serialized_data = serializers.serialize('json', pesanan_konsultasi)
        return JsonResponse({'pesanan': serialized_data}, safe=False)

    elif request.method == 'POST':
        data = request.data
        pesanan_konsultasi = PesananKonsultasi.objects.create(
            pasien=data['pasien'],
            jadwal_konsultasi_id=data['jadwal_konsultasi_id'],
        )
        serialized_data = serializers.serialize('json', [pesanan_konsultasi])
        return JsonResponse({'pesanan': serialized_data}, safe=False)

@login_required(login_url='/login/')
def buat_pesanan(request):
    form = PesananForm()
    data_psikiater = User.objects.filter(role='psychiatrist')

    if request.method == "POST":
        pasien = request.user
        nama_psikiater = request.POST.get('psikiater')
        
        form_data = {
            'user': pasien,
            # Add other form fields here as needed
        }
        
        form = PesananForm(form_data)
        if form.is_valid():
            pesanan = form.save()
            return redirect('pasien:lihat_jadwal_psikiater', psikiater_id=pasien.username)
        
    context = {'form': form, 'dataPsikiater': data_psikiater}
    return render(request, 'buat_pesanan.html', context)

def lihat_jadwal_psikiater(request, psikiater_id):
    if request.method == "GET":
        # psikiater_id = request.GET.get('psikiater_id')
        psikiater = User.objects.get(username=psikiater_id)
        jadwal_objects = Jadwal.objects.filter(psikiater=psikiater)

        context = {'jadwal_objects': jadwal_objects, 'selected_psikiater': psikiater}
        return render(request, 'lihat_jadwal_psikiater.html', {'psikiater_id': psikiater_id})

@login_required(login_url='/login/')
def liat_pesanan(request):
    pesanan = PesananKonsultasi.objects.filter(pasien=request.user)
    return render(request, 'pesanan_konsultasi.html', {'list_pesanan': pesanan})

def buat_pembayaran(request):
    form = PembayaranForm()
    if request.method == 'POST':
        form = PembayaranForm(request.POST, request.FILES)
        data = request.data
        if form.is_valid():
            pembayaran = form.save()
            pembayaran.pasien = data['pasien']
            pembayaran.save()
            img_obj = form.instance

            context = {'form': form, 'img_obj': img_obj}
            return render(request, 'pembayaran.html', context)
        
    context = {'form': form}
    return render(request, 'pembayaran.html', context)