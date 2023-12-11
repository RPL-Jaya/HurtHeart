from django.shortcuts import render, redirect
from .models import Psikiater, Jadwal
from pasien.models import Ulasan
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .forms import JadwalForm
from django.contrib.auth.decorators import login_required
from authentication.models import User

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
            return redirect("/liat-jadwal")
            
    
    context = {"form":form}
    return render(request, "buat_jadwal.html", context)

@login_required(login_url='/login/')
def liat_jadwal(request):
    jadwal = Jadwal.objects.filter(psikiater = request.user)
    print(jadwal)
    context = {"list_jadwal": jadwal}
    return render(request, "list_jadwal.html", context)
