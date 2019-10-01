from django.urls import path
from . import views

urlpatterns = [
    path('reportes/', views.reportes, name='reportes'),
    path('usuarios/', views.usuarios, name='usuarios'),
]
