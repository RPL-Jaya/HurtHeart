from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Pasien, Ulasan, PesananKonsultasi, Pembayaran
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
import base64


# Create your views here.

def buat_ulasan(request):
    print(request)
    form = UlasanForm()
    rating_error = False
    if request.method == 'POST':
        form = UlasanForm(request.POST)
        is_valid = form.is_valid()
        rating_error = form.cleaned_data["rating"] != 5
        if is_valid and not rating_error:
            pesanan_konsultasi_pasien = PesananKonsultasi.objects.get(id=form.cleaned_data["tanggal"])
            Ulasan.objects.create(pasien=Pasien.objects.get(user=request.user),
                                  psikiater=Psikiater.objects.get(user=pesanan_konsultasi_pasien.jadwal_konsultasi.psikiater),
                                  pesanan=pesanan_konsultasi_pasien,
                                  komentar=form.cleaned_data["komentar"],
                                  rating=form.cleaned_data["rating"])
            return redirect('/buat-pesanan')

    pesanan_konsultasi_pasien = PesananKonsultasi.objects.filter(pasien=request.user, status=PesananKonsultasi.DONE, ulasan__isnull=True)
    has_data = len(pesanan_konsultasi_pasien) > 0
    print(pesanan_konsultasi_pasien)
    context = {'form':form, 'pesanan_konsulatasi':pesanan_konsultasi_pasien, 'rating_error':rating_error, 'has_data':has_data}
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
    data_psikiater = User.objects.filter(role='psychiatrist')
    context = {'dataPsikiater': data_psikiater}
    return render(request, 'buat_pesanan.html', context)

def lihat_jadwal_psikiater(request, psikiater_id):
    if request.method == "GET":
        # psikiater_id = request.GET.get('psikiater_id')
        psikiater = User.objects.get(username=psikiater_id)
        jadwal_objects = Jadwal.objects.filter(psikiater=psikiater)

        context = {'jadwal_objects': jadwal_objects, 'selected_psikiater': psikiater, 'psikiater_id': psikiater_id}
        return render(request, 'lihat_jadwal_psikiater.html', context)

@login_required(login_url='/login/')
def liat_pesanan(request):
    pesanan = PesananKonsultasi.objects.filter(pasien=request.user)
    print(pesanan)
    context = {'list_pesanan': pesanan}
    return render(request, 'pesanan_konsultasi.html', context)

def buat_pembayaran(request, jadwal_id):
    form = PembayaranForm()
    if request.method == 'POST':
        form = PembayaranForm(request.POST, request.FILES)
        if form.is_valid():
            byte_data = None
            # Process the image file
            image_file = request.FILES['byte_image']
            with image_file.open('rb') as file:
                byte_data = base64.b64encode(file.read())
                byte_data = byte_data.decode('utf-8')

            pembayaran = Pembayaran.objects.create(pesanan=PesananKonsultasi.objects.get(pasien=request.user, jadwal_konsultasi=Jadwal.objects.get(id=jadwal_id)),
                                      metodePembayaran=form.cleaned_data["metodePembayaran"],
                                      byte_image=byte_data)

            pesanan_konsultasi = pembayaran.pesanan
            pesanan_konsultasi.status = PesananKonsultasi.VERIFY
            pesanan_konsultasi.save()
            return redirect("/pesanan")

    if not PesananKonsultasi.objects.filter(pasien=request.user, jadwal_konsultasi=Jadwal.objects.get(id=jadwal_id)).exists():
        PesananKonsultasi.objects.create(pasien=request.user, jadwal_konsultasi=Jadwal.objects.get(id=jadwal_id))

    jadwal = Jadwal.objects.get(id=jadwal_id)
    context = {'form': form, "jadwal":jadwal}
    return render(request, 'pembayaran.html', context)