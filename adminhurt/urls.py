from django.urls import path
from .views import payment_verification , read_payment

app_name = 'adminhurt'
urlpatterns = [
    path('read-payment/', read_payment, name='read-payment'),
    path('read-payment/<pesanan>', payment_verification, name='payment-verification'),
]
