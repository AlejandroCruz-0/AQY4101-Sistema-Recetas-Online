from django.urls import path
from . import views

urlpatterns = [    
    path('agregar/', views.agregar_medicamento, name='agregar_medicamento'),
    path('listar/', views.listar_medicamentos, name='listar_medicamentos'),
    path('listar/modificar/<int:medicamento_id>/', views.modificar_medicamento, name='modificar_medicamento'),
    path('tipo_medicamentos/', views.tipo_medicamentos, name='tipo_medicamentos'),
    path('tipo_medicamentos/modificar/<int:tipomed_id>', views.tipo_medicamentos_mod, name='tipo_medicamentos_mod'),
    path('tipo_medicamentos/borrar/<int:tipomed_id>', views.tipo_medicamentos_borrar, name='tipo_medicamentos_borrar'),
    path('info_medicamento/<int:medicamento_id>', views.info_medicamento, name='info_medicamento'),
    

]