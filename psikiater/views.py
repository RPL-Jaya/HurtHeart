<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Psikiater, JadwalKonsultasi
from pasien.models import Ulasan
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
=======
from django.shortcuts import render
from .models import Psikiater, Jadwal
from pasien.models import Ulasan
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .forms import JadwalForm
from django.contrib.auth.decorators import login_required
from authentication.models import User
>>>>>>> 4b31391a29a08c132228cd6f7758e92ba5c2bef2

# Create your views here.


# Profile View
def psikiater_detail(request, username):
    # Get psikiater by id
    psikiater = Psikiater.objects.get(username=username)
    ulasan = Ulasan.objects.filter(psikiater=psikiater)
    context = {'psikiater': psikiater, 'ulasan_list': ulasan}
    return render(request, 'profile.html', context)

def psikiater_detail_api(request, username):
    # Get psikiater by id
    psikiater = Psikiater.objects.get(username=username)
    ulasan = Ulasan.objects.filter(psikiater=psikiater)
    context = {'psikiater': model_to_dict(psikiater), 'ulasan_list': [model_to_dict(ulasan) for ulasan in ulasan]}
    # Return psikiater detail in JSON format
    return JsonResponse(context)


# List of psikiater
def psikiater_list(request):
    # Get all psikiater
    psikiater = Psikiater.objects.list_psikiater()
    context = {'psikiater_list': psikiater}
    return render(request, 'list.html', context)

def psikiater_list_api(request):
    # Get all psikiater
    psikiater = Psikiater.objects.all()
    context = {'psikiater_list': [model_to_dict(psikiater) for psikiater in psikiater]}
    # Return psikiater list in JSON format
    return JsonResponse(context)

<<<<<<< HEAD
@api_view(['GET', 'POST'])
@csrf_exempt
def jadwal_konsultasi_list_create(request):
    if request.method == 'GET':
        jadwal_konsultasi = JadwalKonsultasi.objects.all()
        serialized_data = serializers.serialize('json', jadwal_konsultasi)
        return JsonResponse({'jadwal_konsultasi': serialized_data}, safe=False)

    elif request.method == 'POST':
        data = request.data
        jadwal_konsultasi = JadwalKonsultasi.objects.create(
            psikiater=data['psikiater'],
            tanggal=data['tanggal'],
            ketersediaan=data['ketersediaan'],
        )
        serialized_data = serializers.serialize('json', [jadwal_konsultasi])
        return JsonResponse({'jadwal_konsultasi': serialized_data}, safe=False)
    
    
=======
@login_required(login_url='/login/')
def add_jadwal(request):
    form = JadwalForm()
    if request.method == "POST":
        form = JadwalForm(request.POST)
        if form.is_valid():
            tanggal = form.cleaned_data["tanggal"]
            jam_mulai = form.cleaned_data["jam_mulai"]
            jam_selesai = form.cleaned_data["jam_selesai"]
            metode = form.cleaned_data["metode"]
            keterangan = form.cleaned_data["keterangan"]
            kuota_total = form.cleaned_data["kuota_total"]
            Jadwal.objects.create(psikiater = request.user,tanggal = tanggal, jam_mulai = jam_mulai, jam_selesai = jam_selesai, metode = metode, keterangan = keterangan, kuota_total = kuota_total, kuota_tersedia = kuota_total)
            print("saved")
            
    
    context = {"form":form}
    return render(request, "buat_jadwal.html", context)

@login_required(login_url='/login/')
def liat_jadwal(request):
    jadwal = Jadwal.objects.filter(psikiater = request.user)
>>>>>>> 4b31391a29a08c132228cd6f7758e92ba5c2bef2
