from django.urls import path
from caloriecounter import views


urlpatterns = [
path('', views.home, name="home"),
path('add/', views.add, name="add"),
path('nutrition/<int:obj>/', views.nutrition, name="nutrition"),

]