from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse


from .models import Pasien, Ulasan
from .forms import UlasanForm

from psikiater.models import Psikiater

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