from django.urls import path
<<<<<<< HEAD
from .views import psikiater_detail, psikiater_detail_api, psikiater_list, psikiater_list_api, jadwal_konsultasi_list_create
=======
from .views import psikiater_detail, psikiater_detail_api, psikiater_list, psikiater_list_api, add_jadwal
>>>>>>> 4b31391a29a08c132228cd6f7758e92ba5c2bef2

app_name = 'psikiater'
urlpatterns = [
    path('psikiater/', psikiater_list, name='psikiater_list'),
    path('api/psikiater/', psikiater_list_api, name='psikiater_list_api'),
    path('psikiater/<str:username>', psikiater_detail, name='psikiater_detail'),
    path('api/psikiater/<str:username>', psikiater_detail_api, name='psikiater_detail_api'),
<<<<<<< HEAD
    path('jadwal/', jadwal_konsultasi_list_create, name='jadwal-list-create'),

=======
    path("addJadwal", add_jadwal, name="addJadwal"), 
>>>>>>> 4b31391a29a08c132228cd6f7758e92ba5c2bef2
]
