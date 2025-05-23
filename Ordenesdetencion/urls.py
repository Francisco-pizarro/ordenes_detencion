from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('login/', views.login_view, name='login'), 
    path('accounts/login/', views.login_view, name='accounts_login'),  # <--- AÑADE ESTA LÍNEA
]
