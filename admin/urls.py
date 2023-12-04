from django.urls import path
from .views import payment_verification

app_name = 'pasien'
urlpatterns = [
    path('payment/', payment_verification, name='payment-verification'),
]
