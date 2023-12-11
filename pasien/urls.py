from django.urls import path
from . import views
from .views import buat_ulasan, buat_ulasan_api, pesanan_konsultasi_pasien, buat_pembayaran, buat_pesanan, lihat_jadwal_psikiater

app_name = 'pasien'
urlpatterns = [
    path('ulas/', buat_ulasan, name='ulas'),
    path('api/ulas/', buat_ulasan_api, name='ulas_api'),
    path('pesanan/', pesanan_konsultasi_pasien, name='pesanan-list-pasien'),
    path('pembayaran/', buat_pembayaran, name='buat_pembayaran'),
    path('buat-pesanan/', buat_pesanan, name='buat_pesanan'),
    path('lihat-jadwal-psikiater/<str:psikiater_id>/', lihat_jadwal_psikiater, name='lihat_jadwal_psikiater'),
]
