from django.shortcuts import render
from pasien.models import Pembayaran
from django.contrib.auth.decorators import login_required

# Create your views here.

# create view for payment verification
@login_required(login_url='/login/')
def payment_verification(request,pk):
    if request.method == "POST" and 'btn-accept' in request.POST:    
        # get all payment data
        payment = Pembayaran.objects.filter(id=pk).update(statusPembayaran=True)
        # create context
        context = {
            "payment":payment
        }
    elif request.method == "POST" and 'btn-reject' in request.POST:
        # get all payment data
        payment = Pembayaran.objects.filter(id=pk).update(statusPembayaran=False)
        # create context
        context = {
            "payment":payment
        }
    # render page
    return render(request,"admin/payment_verification.html",context)