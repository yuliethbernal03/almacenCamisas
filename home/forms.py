from django import forms
from .models import *

class contacto_form(forms.Form):
    correo = forms.EmailField(widget = forms.TextInput())
    titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea())

class agregar_tEstampado_form(forms.ModelForm):
    class Meta:
        model = Estampados
        fields = '__all__'

class agregar_tCamisa_form(forms.ModelForm):
    class Meta:
        model = Camisa
        fields = '__all__'

class agregar_tTela_form(forms.ModelForm):
    class Meta:
        model = Tela
        fields = '__all__'

class login_form(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput())
    clave = forms.CharField(widget=forms.PasswordInput(render_value=False))