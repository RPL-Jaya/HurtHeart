from django.shortcuts import render, get_object_or_404
from .models import Psikiater, JadwalKonsultasi
from pasien.models import Ulasan
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import JadwalKonsultasiForm
from django.contrib.auth.decorators import login_required

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

@login_required
def jadwal_konsultasi_psikiater(request):
    if request.user.role != 'psychiatrist':
        return redirect('authentication:login')
    if request.method == 'POST':
        form = JadwalKonsultasiForm(request.POST)
        if form.is_valid():
            jadwal_konsultasi = form.save(commit=False)
            jadwal_konsultasi.psikiater = request.user
            jadwal_konsultasi.save()
            return redirect('psikiater:jadwal_konsultasi_psikiater')
    else:
        form = JadwalKonsultasiForm()

    jadwal_konsultasi_list = JadwalKonsultasi.objects.filter(psikiater=request.user)
    context = {'form': form, 'jadwal_konsultasi_list': jadwal_konsultasi_list}
    return render(request, 'jadwal_konsultasi.html', context)


    