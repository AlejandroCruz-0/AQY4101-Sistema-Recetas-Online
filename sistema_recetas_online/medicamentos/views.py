from django.shortcuts import render

# Create your views here.
def agregar_medicamento(request):

    return render(request, 'agregar_medicamento.html')

def listar_medicamentos(request):

    return render(request, 'listar_medicamentos.html')