from django.urls import path
from . import views

urlpatterns = [    
    path('agregar/', views.agregar_medicamento, name='agregar_medicamento'),
    path('listar/', views.listar_medicamentos, name='listar_medicamentos'),
]