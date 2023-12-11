from django.urls import path
from .views import buat_ulasan, buat_ulasan_api, pesanan_konsultasi_pasien, buat_pembayaran, buat_pesanan, lihat_jadwal_psikiater, liat_pesanan

app_name = 'pasien'
urlpatterns = [
    path('ulas/', buat_ulasan, name='ulas'),
    path('api/ulas/', buat_ulasan_api, name='ulas_api'),
    path('pesanan/', liat_pesanan, name='list_pesanan'),
    path('pembayaran/<str:jadwal_id>/', buat_pembayaran, name='buat_pembayaran'),
    path('buat-pesanan/', buat_pesanan, name='buat_pesanan'),
    path('lihat-jadwal-psikiater/<str:psikiater_id>/', lihat_jadwal_psikiater, name='lihat_jadwal_psikiater'),
]
