from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, logout
from .forms import RegisterForm
from .models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from psikiater.models import Psikiater, Jadwal
from pasien.models import Pasien, Ulasan, PesananKonsultasi, Pembayaran

# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST.get('password'))
            user.save()
            if user.role == "psychiatrist":
                Psikiater.objects.create(user=user)
            elif user.role == "patient":
                Pasien.objects.create(user=user)
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
            elif user.role == "patient":
                return redirect("/pesanan")
            return redirect('/read-payment')

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

def clear_data(request):

    Jadwal.objects.all().delete()
    Ulasan.objects.all().delete()
    PesananKonsultasi.objects.all().delete()
    Pembayaran.objects.all().delete()
    return render(request, "test.html")

def refresh_role(request):
    for user in User.objects.all():
        print(user)
        if user.role == "psychiatrist":
                if not Psikiater.objects.filter(user=user).exists():
                    Psikiater.objects.create(user=user)
        elif user.role == "patient":
            if not Pasien.objects.filter(user=user).exists():
                    Pasien.objects.create(user=user)
    return render(request, "test.html")
