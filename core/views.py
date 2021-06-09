from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .decorators import unauthenticated_user

def home(request):
    return render(request, 'core/index.html')

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home_finance')
        else:
            messages.info(request, 'Usuario O/Y Contraseña Es Incorrecto')
    
    context = {}
    return render(request, 'core/login.html', context)

def logoutSite(request):
    logout(request)
    return redirect('login')

def password_reset(request):
    return render(request, 'core/reset_password.html')