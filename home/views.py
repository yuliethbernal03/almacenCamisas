from django.shortcuts import render
from .forms import *

# Create your views here.
def home_view(request):
    msg = 'pagina de inicio'
    return render(request, 'home.html', locals())

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    email = ""
    title = ""
    text  = ""
    enviado = False
    if request.method == 'POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            enviado = True
            email = formulario.cleaned_data['correo']
            title = formulario.cleaned_data['titulo']
            text = formulario.cleaned_data['texto']
    else:
        formulario = contacto_form()

    return render (request, 'contact.html', locals())
