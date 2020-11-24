from django.shortcuts import render, redirect, get_object_or_404
from .models import Info_Medicamentos, Medicamentos, Tipo_Medicamento
from .forms import FormAgregarMedicamento, FormInfo_Medicamento, FormTipo_Medicamento
from django.urls import reverse

# Create your views here.
def agregar_medicamento(request):

    formulario = FormAgregarMedicamento()
    
    if request.method == 'POST':
        #Solicitud post rellenar formulario
        formulario = FormAgregarMedicamento(data=request.POST)
        

        if formulario.is_valid():
            objMedicamento = formulario.save()            
            medicamento_id = objMedicamento.pk
            return redirect('info_medicamento',medicamento_id=medicamento_id )
            
    return render(request, 'agregar_medicamento.html', {'form': formulario})

def tipo_medicamentos(request):
    
    formulario = FormTipo_Medicamento()
    tipo_medicamentos = Tipo_Medicamento.objects.all()

    if request.method == 'POST':
        formulario = FormTipo_Medicamento(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('tipo_medicamentos'))

    return render(request, 'tipo_medicamentos.html',{'form':formulario,'tipo_medicamentos':tipo_medicamentos})        

def tipo_medicamentos_mod(request,tipomed_id):

    tm = get_object_or_404(Tipo_Medicamento, id_Tipo_Medicamento=tipomed_id)
    formulario = FormTipo_Medicamento(instance=tm)    

    if request.method == 'POST':
        formulario = FormTipo_Medicamento(data=request.POST, instance=tm)        
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('tipo_medicamentos'))

    return render(request, 'editar_tipo_medicamento.html',{'form':formulario})        

def tipo_medicamentos_borrar(request, tipomed_id):

    tipo_medicamento = get_object_or_404(Tipo_Medicamento, id_Tipo_Medicamento=tipomed_id)

    
    try:
        tipo_medicamento.delete()
        return redirect(reverse('tipo_medicamentos')+"?exito")
    except Exception as e:        
        return redirect(reverse('tipo_medicamentos')+"?error")   
        
    

def info_medicamento(request, medicamento_id):

    formulario = FormInfo_Medicamento()


    if request.method == 'POST':
        #Solicitud post rellenar formulario
        medicamento = Medicamentos.objects.get(id_Medicamento=medicamento_id)
        formulario = FormInfo_Medicamento(data=request.POST)

        if formulario.is_valid():
            info_med = formulario.save(commit=False)
            info_med.pk = medicamento.pk
            info_med.save()
            return redirect(reverse('listar_medicamentos'))





    return render(request, 'info_medicamento.html',{'form':formulario,'medicamento_id':medicamento_id})

def listar_Tipo_Medicamento(request):
    lt_medicamentos = Tipo_Medicamento.objects.all()
    return render(request, 'listar_medicamentos.html',{'detalle_med':lt_medicamentos})

def listar_medicamentos(request):
    l_medicamentos = Medicamentos.objects.all()
    f = FormAgregarMedicamento()
    return render(request, 'listar_medicamentos.html',{'medicamentos':l_medicamentos,'form':f})

def modificar_medicamento(request, medicamento_id):
    l_medicamentos = Medicamentos.objects.all()
    m = get_object_or_404(Medicamentos,id_Medicamento=medicamento_id)
    f = FormAgregarMedicamento(instance=m)

    if request.method == 'POST':
        f = FormAgregarMedicamento(data=request.POST, instance=m)        
        if f.is_valid():
            f.save()
            return redirect(reverse('listar_medicamentos'))


    return render(request, 'listar_medicamentos.html',{'medicamentos':l_medicamentos,'form':f})



    
