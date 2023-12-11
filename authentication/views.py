from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, logout
from .forms import RegisterForm
from .models import User
import sys
sys.path.append("..")
from psikiater.models import Psikiater
from pasien.models import Pasien

# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST.get('password'))
            user.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('authentication:login')
        print(form.errors)
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == "psychiatrist":
                return redirect("/liat-jadwal")
            return redirect('authentication:test')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect("/")
def test(request):
    print(User.objects.all())
    return render(request, "test.html")

def home(request):
    return render(request, "home.html")
