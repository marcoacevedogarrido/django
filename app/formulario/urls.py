from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.formulario_create, name='formulario_create' ),
    path('edit/<int:id_formulario>/', views.formulario_edit, name='formulario_edit' ),
    path('delete/<int:id_formulario>/', views.formulario_delete, name='formulario_delete' ),

]
