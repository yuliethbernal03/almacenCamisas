from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate

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
    
def shirt_print_view(request):
    listShirtPrint = Estampados.objects.filter()
    return render (request, 'shirt_prin.html', locals())

def shirts_view(request):
    listShirts = Camisa.objects.filter()
    return render (request, 'shirts.html', locals())

def fabrics_view(request):
    listFabrics = Tela.objects.filter()
    return render (request, 'fabrics.html', locals())

def add_shirt_print_view(request):
    if request.method == 'POST':
        formulario = agregar_tEstampado_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/shirt_print/')
    else:
        formulario =  agregar_tEstampado_form()

    return render (request, 'add_shirt_print.html', locals())

def add_tShirt_view(request):
    if request.method == 'POST':
        formulario = agregar_tCamisa_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/shirts/')
    else:
        formulario = agregar_tCamisa_form()

    return render (request, 'add_tShirt.html', locals())

def add_tFabric_view(request):
    if request.method == 'POST':
        formulario = agregar_tTela_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/fabrics/')
    else:
        formulario = agregar_tTela_form()

    return render (request, 'add_tFabric.html', locals())

def see_shirt_print_view(request, id_print):
    detalle = Estampados.objects.get(id=id_print)
    return render(request, 'see_shirt_print.html', locals())

def remove_shirt_print_view(request, id_print):
    objeto = Estampados.objects.get(id=id_print)
    objeto.delete()
    return redirect ('/shirt_print/')

def edit_shirt_print_view(request, id_print):
    objeto = Estampados.objects.get(id=id_print)
    if request.method == 'POST':
        formulario  = agregar_tEstampado_form(request.POST, request.FILES, instance = objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/shirt_print/')
    else:
        formulario = agregar_tEstampado_form(instance = objeto)
    return render (request, 'add_shirt_print.html', locals())

def remove_tShirt_view(request, id_shirt):
    objeto = Camisa.objects.get(id=id_shirt)
    objeto.delete()
    return redirect ('/shirts/')

def edit_tShirt_view(request, id_shirt):
    objeto = Camisa.objects.get(id = id_shirt)
    if request.method == 'POST':
        formulario  = agregar_tCamisa_form(request.POST, request.FILES, instance = objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/shirts/')
    else:
        formulario = agregar_tCamisa_form(instance = objeto)
    return render (request, 'add_tShirt.html', locals())

def remove_tFabric_view(request, id_fabric):
    objeto = Tela.objects.get(id=id_fabric)
    objeto.delete()
    return redirect ('/fabrics/')

def edit_tFabric_view(request, id_fabric):
    objeto = Tela.objects.get(id = id_fabric)
    if request.method == 'POST':
        formulario  = agregar_tTela_form(request.POST, request.FILES, instance = objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/fabrics/')
    else:
        formulario = agregar_tTela_form(instance = objeto)
    return render (request, 'add_tFabric.html', locals())

def login_view(request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username = usu, password = cla)
            if usuario  is not None and usuario.is_active:
                login(request, usuario)
                return redirect ('/')
            else:
                msj = "Usuario o clave incorrectos."
    else:
        formulario = login_form()
    return render(request, 'login.html', locals())

def logout_view(request):
    logout(request)
    return redirect('/login/')