from django.urls import path
from . import views


urlpatterns = [
    path('', views.candles),
    path('candle/<str:pk>/', views.candle),
    path('register/', views.register),
    path('login/', views.login)
]