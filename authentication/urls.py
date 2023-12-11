from django.urls import path
from authentication.views import *

app_name = 'authentication'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name="logout"),
    path("test/", test, name="test"),
    path("clear-data/", clear_data, name="clear_data"),
    path("", home, name="home")
]
