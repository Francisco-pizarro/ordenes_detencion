from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('rojo', views.resultado),
    path('verde', views.resultadok),
    
] 