from django.urls import path
from .views import payment_verification

app_name = 'adminhurt'
urlpatterns = [
    path('payment-verification/', payment_verification, name='payment-verification'),
]
