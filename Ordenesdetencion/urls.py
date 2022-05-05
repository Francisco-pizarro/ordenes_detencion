from django.urls import path, include
from.views import index,resultado,resultadok
urlpatterns = [
    path('', index, name= 'inicio'),
    path('resultado/', resultado, name= 'resultado'),
    path('resultadok/', resultadok, name= 'resultadok'),
    
] 