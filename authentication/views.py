from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                username=user,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                date_of_birth=user.date_of_birth,
                role=user.role
            )
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
        print(user)
        if user is not None:
            login(request, user)
            return redirect('authentication:test')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def test(request):
    return render(request, "test.html")
