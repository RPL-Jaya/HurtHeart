from django.shortcuts import render
from pasien.models import Pembayaran, PesananKonsultasi
from psikiater.models import Jadwal
from django.contrib.auth.decorators import login_required

# Create your views here.

# create view for payment verification
@login_required(login_url='/login/')
def payment_verification(request,pk):
    # get all payment data
    payment = Pembayaran.objects.filter(id=pk)
    if request.method == "POST" and 'btn-accept' in request.POST:    
        # get all payment data
        payment.update(statusPembayaran=True)
        # create context
        context = {
            "payment":payment
        }
    elif request.method == "POST" and 'btn-reject' in request.POST:
        # get all payment data
        payment.update(statusPembayaran=False)
        # create context
        context = {
            "payment":payment
        }
    # render page
    return render(request,"verifikasipembayaran.html",context)

# create view for reading Pembayaran model
@login_required(login_url='/login/')
def read_payment(request):
    # get all payment data
    payment = Pembayaran.objects.all()
    # create context
    context = {
        "pembayaran_list":payment,
    }
    # render page
    return render(request,"read-payment.html",context)