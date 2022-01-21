import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Candle

# Create your views here.


def candles(request):
    candles = Candle.objects.all().order_by('date')
    return render(request, 'index.html', {'candles' : candles})

def candle(request, pk):
    return HttpResponse('Candle page: ' + str(pk))


def products(request):
    return render(request, 'producten.html')
