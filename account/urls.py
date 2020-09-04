from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.account_info, name='acc-info'),
    path('logout/', views.logout_profile, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.registration, name='register')
]