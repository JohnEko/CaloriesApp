from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registeration, name='register'),
    path('mailsend/', views.mailsend, name='mail'),
    path('login/', views.login_page, name='login'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    
]

