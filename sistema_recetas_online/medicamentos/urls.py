from django.urls import path
from . import views

urlpatterns = [    
    path('', views.agregar_medicamento, name='agregar_medicamento'),
]