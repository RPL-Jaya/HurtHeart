from django.shortcuts import render, redirect
from pasien.models import Pembayaran, PesananKonsultasi
from psikiater.models import Jadwal
from django.contrib.auth.decorators import login_required

# Create your views here.

# create view for payment verification
@login_required(login_url='/login/')
def payment_verification(request,pk):
    # get all payment data
    payment = Pembayaran.objects.get(id=pk)
    print(payment)
    context = {
        "payment":payment,
    }
    # render page
    return render(request,"verifikasipembayaran.html",context)

# create view for reading Pembayaran model
@login_required(login_url='/login/')
def read_payment(request):
    # get all payment data
    payment = Pembayaran.objects.filter(statusPembayaran=False)
    # create context
    context = {
        "pembayaran_list":payment,
    }
    # render page
    return render(request,"read-payment.html",context)

def accept(request,pk):
    payment = Pembayaran.objects.get(id=pk)
    payment.statusPembayaran = True
    payment.save()

    pesanan_konsultasi = payment.pesanan
    pesanan_konsultasi.status = PesananKonsultasi.SCHED
    pesanan_konsultasi.save()

    jadwal = payment.pesanan.jadwal_konsultasi
    jadwal.kuota_tersedia -=1
    jadwal.save()
    
    return redirect("/read-payment")

def reject(request,pk):
    payment = Pembayaran.objects.get(id=pk)
    pesanan_konsultasi = payment.pesanan
    payment.delete()
    pesanan_konsultasi.delete()
    return redirect("/read-payment")