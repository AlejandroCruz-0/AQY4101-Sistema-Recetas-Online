from django.forms import ModelForm, TextInput, Select, NumberInput, ModelChoiceField
from .models import Medicamentos,Tipo_Medicamento,Info_Medicamentos

class FormAgregarMedicamento(ModelForm):
    
    
    class Meta:
        model = Medicamentos
        fields = ['Nombre', 'Marca','Laboratorio'
        , 'Cantidad_de_comprimidos', 'Gramaje', 'id_Tipo_medicamento']
        widgets ={
            'Nombre': TextInput(attrs={'id':'nombreMed-txt','class':'form-control form-control-sm','placeholder':'Nombre Medicamento'}),
            'Marca': TextInput(attrs={'id':'marcaMed-txt','class':'form-control form-control-sm','placeholder':'Marca Medicamento'}),
            'Laboratorio': TextInput(attrs={'id':'labMed-txt','class':'form-control form-control-sm','placeholder':'Laboratorio Medicamento'}),
            'Cantidad_de_comprimidos': NumberInput(attrs={'id':'cantCom-Num','class':'form-control form-control-sm'
            ,'placeholder':'Cantidad de comprimidos'}),
            'Gramaje': NumberInput(attrs={'id':'GramajeMed-Num','class':'form-control form-control-sm','placeholder':'Gramaje Medicamento'}),            
            'id_Tipo_medicamento': Select(attrs={'class':'form-select','placeholder':'Tipo medicamento'}),
            
            
        }