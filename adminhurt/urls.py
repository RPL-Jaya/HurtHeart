from django.urls import path
from .views import payment_verification , read_payment

app_name = 'adminhurt'
urlpatterns = [
    path('payment-verification/', payment_verification, name='payment-verification'),
    path('read-payment/', read_payment, name='read-payment'),
]
