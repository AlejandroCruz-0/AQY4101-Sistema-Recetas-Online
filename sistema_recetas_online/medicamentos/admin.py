from django.contrib import admin
from .models import Medicamentos,Tipo_Medicamento, Info_Medicamentos
# Register your models here.

class MedicamentoAdmin(admin.ModelAdmin):
    pass

class Tipo_MedicamentoAdmin(admin.ModelAdmin):
    pass

class Info_MedicamentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medicamentos,MedicamentoAdmin)
admin.site.register(Tipo_Medicamento,Tipo_MedicamentoAdmin)
admin.site.register(Info_Medicamentos,Info_MedicamentoAdmin)