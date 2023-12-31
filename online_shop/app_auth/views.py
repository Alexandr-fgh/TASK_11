from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
# Create your views here.
@login_required(login_url= reverse_lazy("login"))
def profile_view(request):
    return render(request, 'app_auth/profile.html' )
    



def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username, password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error':'Пользаватель не найден'})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))