import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candle
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.


def candles(request):
    candles = Candle.objects.all().order_by('date')
    return render(request, 'index.html', {'candles' : candles})

def candle(request, pk):
    return HttpResponse('Candle page: ' + str(pk))


def products(request):
    return render(request, 'producten.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')

    context = {'form' : form}
    return render(request, 'registratie.html', context)

def login(request):
    return render(request, 'login.html')