from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.candles, name = 'index'),
    path('candle/<str:pk>/', views.candle),
    path('register/', views.registerPage),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout')
]