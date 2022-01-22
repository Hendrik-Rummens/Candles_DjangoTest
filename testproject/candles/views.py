import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candle
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def candles(request):
    candles = Candle.objects.all().order_by('date')
    return render(request, 'index.html', {'candles' : candles})

def candle(request, pk):
    return HttpResponse('Candle page: ' + str(pk))


def products(request):
    return render(request, 'producten.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account gecreëerd voor ' + username)
            return redirect('login')

    context = {'form' : form}
    return render(request, 'registratie.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Gebruikersnaam of wachtwoord is fout')
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'Gebruiker is succesvol uitgelogd.')
    return redirect('index')