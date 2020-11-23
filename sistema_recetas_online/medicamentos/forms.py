from django.forms import ModelForm, TextInput, Select, NumberInput, ModelChoiceField, CheckboxInput
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


class FormInfo_Medicamento(ModelForm):

    class Meta:
        model = Info_Medicamentos
        fields = ['Formula','Advertencias','Indicaciones',
        'Contra_Indicaciones','Bioequivalente']
        widgets ={
            'Formula': TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Formula Medicamento'}),
            'Advertencias': TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Advertencias Medicamento'}),
            'Indicaciones': TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Indicaciones Medicamento'}),
            'Contra_Indicaciones': TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Contra_Indicaciones Medicamento'}),
            'Bioequivalente': CheckboxInput(attrs={'class':'form-check-input','type':'checkbox','id':'bioequivalente-chkbox'},)
                
            }

class FormTipo_Medicamento(ModelForm):
    class Meta:
        model = Tipo_Medicamento
        fields = ['Nombre_Tipo_Medicamento']
        widgets ={
            'Nombre_Tipo_Medicamento': TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Nombre tipo Medicamento'}),

        }