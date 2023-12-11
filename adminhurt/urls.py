from django.urls import path
from .views import *

app_name = 'adminhurt'
urlpatterns = [
    path('read-payment/', read_payment, name='read-payment'),
    path('detail/<int:pk>/', payment_verification, name='payment-verification'),
    path('reject/<int:pk>/', reject, name='reject'),
    path('accept/<int:pk>/', accept, name='accept'),
]
