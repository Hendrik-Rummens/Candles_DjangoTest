from django.urls import path
from . import views


urlpatterns = [
    path('', views.candles),
    path('candle/<str:pk>/', views.candle)
]