from django import forms
from django.contrib.auth.models import User
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

class registro_form(forms.Form):
    username = forms.CharField(widget = forms.TextInput())
    email = forms.EmailField(widget = forms.TextInput())
    password_1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(render_value=False))
    password_2 = forms.CharField(label = 'Confirmar Password', widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya registrado.')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            e = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Correo electronico ya registrado.')

    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']

        if password_1==password_2:
            pass
        else:
            raise forms.ValidationError('La contraseña no coincide.')