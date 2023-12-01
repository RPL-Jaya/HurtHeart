from django.urls import path
from .views import psikiater_detail, psikiater_detail_api

app_name = 'psikiater'
urlpatterns = [
    # API /api/psikiater/{id}
    path('psikiater/<str:username>', psikiater_detail, name='psikiater_detail'),
    path('api/psikiater/<str:username>', psikiater_detail_api, name='psikiater_detail_api'),
]
