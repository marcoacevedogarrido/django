from django import forms
from .models import Formulario, Formulario_id

class FormularioForm(forms.ModelForm):

    class Meta:
        model = Formulario
        fields = [
            'id',
            'dato1',
            'dato2',
            'dato3',
        ]
        labels = {
            'id':'Id',
            'dato1':'Dato 1',
            'dato2':'Dato 2',
            'dato3':'Dato 3',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'dato1': forms.TextInput(attrs={'class':'form-control'}),
            'dato2': forms.TextInput(attrs={'class':'form-control'}),
            'dato3': forms.TextInput(attrs={'class':'form-control'}),
        }

class InformeForm(forms.ModelForm):

    class Meta:
        model = Formulario_id
        fields = [
            'id_inicio',
            'id_fin',
        ]
        labels = {
            'id_inicio':'id_inicio',
            'id_fin':'id_fin',
        }
        widgets = {
            'id_inicio': forms.DateInput(attrs={'class':'form-control'}),
            'id_fin': forms.DateInput(attrs={'class':'form-control'}),
        }
