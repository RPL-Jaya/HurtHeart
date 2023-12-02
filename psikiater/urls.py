from django.urls import path
from .views import psikiater_detail, psikiater_detail_api, psikiater_list, psikiater_list_api

app_name = 'psikiater'
urlpatterns = [
    path('psikiater/', psikiater_list, name='psikiater_list'),
    path('api/psikiater/', psikiater_list_api, name='psikiater_list_api'),
    path('psikiater/<str:username>', psikiater_detail, name='psikiater_detail'),
    path('api/psikiater/<str:username>', psikiater_detail_api, name='psikiater_detail_api'),

]
