from django.urls import path
from .views import buat_ulasan, buat_ulasan_api, pesanan_konsultasi, buat_pembayaran, buat_pesanan

app_name = 'pasien'
urlpatterns = [
    path('ulas/', buat_ulasan, name='ulas'),
    path('api/ulas/', buat_ulasan_api, name='ulas_api'),
    path('pesanan/', pesanan_konsultasi, name='pesanan-list-pasien'),
    path('pembayaran/', buat_pembayaran, name='buat_pembayaran'),
    path('buat-pesanan/', buat_pesanan, name='buat_pesanan')
]
