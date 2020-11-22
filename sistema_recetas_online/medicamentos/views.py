from django.shortcuts import render, redirect
from .models import Info_Medicamentos, Medicamentos, Tipo_Medicamento
from .forms import FormAgregarMedicamento
from django.urls import reverse

# Create your views here.
def agregar_medicamento(request):

    formulario = FormAgregarMedicamento()
    
    if request.method == 'POST':
        #Solicitud post rellenar formulario
        formulario = FormAgregarMedicamento(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('agregar_medicamento'))
    return render(request, 'agregar_medicamento.html', {'form': formulario})