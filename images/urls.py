from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.image_create, name='create'),
    # path('create/', views.CreatePostView.as_view(), name='create'),
    path('detail/<slug:slug>/', views.image_detail, name='detail'),
    path('', views.image_list, name='image_list'),
]