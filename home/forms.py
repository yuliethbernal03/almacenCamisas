from django import forms
from .models import *

class contacto_form(forms.Form):
    correo = forms.EmailField(widget = forms.TextInput())
    titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea())

class agregar_tEstampado_form(forms.ModelForm):
    class Meta:
        model = DatosProducto
        fields = '__all__'

class agregar_tCamisa_form(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class agregar_tTela_form(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'