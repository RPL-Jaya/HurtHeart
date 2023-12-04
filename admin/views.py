from django.shortcuts import render
from pasien.models import Pembayaran

# Create your views here.
# create view for payment verification
def payment_verification(request):
    # get all payment data
    payment = Pembayaran.objects.filter().update(statusPembayaran=True)
    # create context
    context = {
        "payment":payment
    }
    # render page
    return render(request,"admin/payment_verification.html",context)