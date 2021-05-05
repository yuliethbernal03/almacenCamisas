from django.shortcuts import render, redirect
from .forms import *
from .models import *

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
    
def products_view(request):
    listProducts = DatosProducto.objects.filter()
    return render (request, 'products.html', locals())

def shirts_view(request):
    listShirts = Pedido.objects.filter()
    return render (request, 'shirts.html', locals())

def fabrics_view(request):
    listFabrics = Categoria.objects.filter()
    return render (request, 'fabrics.html', locals())

def add_product_view(request):
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/products/')
    else:
        formulario = agregar_producto_form()

    return render (request, 'add_product.html', locals())

def add_tShirt_view (request):
    if request.method == 'POST':
        formulario = agregar_tCamisa_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/shirts/')
    else:
        formulario = agregar_tCamisa_form()

    return render (request, 'add_tShirt.html', locals())

def add_tFabric_view (request):
    if request.method == 'POST':
        formulario = agregar_tTela_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/fabrics/')
    else:
        formulario = agregar_tTela_form()

    return render (request, 'add_tFabric.html', locals())

def see_product_view (request, id_prod):
    detalle = DatosProducto.objects.get(id=id_prod)
    return render(request, 'see_product.html', locals())

def remove_product_view (request, id_prod):
    objeto = DatosProducto.objects.get(id=id_prod)
    objeto.delete()
    return redirect ('/products/')

def edit_product_view (request, id_prod):
    objeto = DatosProducto.objects.get(id = id_prod)
    if request.method == 'POST':
        formulario  = agregar_producto_form(request.POST, request.FILES, instance = objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/products/')
    else:
        formulario = agregar_producto_form(instance = objeto)
    return render (request, 'add_product.html', locals())

def remove_tShirt_view (request, id_shirt):
    objeto = Pedido.objects.get(id=id_shirt)
    objeto.delete()
    return redirect ('/shirts/')

def edit_tShirt_view (request, id_shirt):
    objeto = Pedido.objects.get(id = id_shirt)
    if request.method == 'POST':
        formulario  = agregar_tCamisa_form(request.POST, request.FILES, instance = objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/shirts/')
    else:
        formulario = agregar_tCamisa_form(instance = objeto)
    return render (request, 'add_tShirt.html', locals())

def remove_tFabric_view (request, id_fabric):
    objeto = Categoria.objects.get(id=id_fabric)
    objeto.delete()
    return redirect ('/fabrics/')

def edit_tFabric_view (request, id_fabric):
    objeto = Categoria.objects.get(id = id_fabric)
    if request.method == 'POST':
        formulario  = agregar_tTela_form(request.POST, request.FILES, instance = objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/fabrics/')
    else:
        formulario = agregar_tTela_form(instance = objeto)
    return render (request, 'add_tFabric.html', locals())
 
