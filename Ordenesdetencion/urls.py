from django.urls import path, include
from.views import index,resultado
urlpatterns = [
    path('', index, name= 'inicio'),
    path('resultado/', resultado, name= 'resultado'),
    
] 