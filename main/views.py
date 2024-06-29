from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Carrito
from .forms import UsuarioForm, CarritoForm


def mostrar_index(request):
    return render(request,'main/index.html')

def mostrar_regis(request):
    return render(request,'main/registrarse.html')

def mostrar_carrito(request):
    return render(request, 'main/carrito.html')

def mostrar_herramientas(request):
    return render(request,'main/herramientas.html')

def mostrar_jardineria(request):
    return render(request,'main/jardineria.html')

def mostrar_nosotros(request):
    return render(request,'main/nostros.html')

def mostrar_sesion(request):
    return render(request,'main/sesion.html')

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'main/usuario_list.html', {'usuarios': usuarios})

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'main/usuario_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'main/usuario_form.html', {'form': form})

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'main/usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'main/usuario_confirm_delete.html', {'usuario': usuario})

# CRUD para Carrito
def carrito_list(request):
    carritos = Carrito.objects.all()
    return render(request, 'main/carrito_list.html', {'carritos': carritos})

def carrito_create(request):
    if request.method == 'POST':
        form = CarritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carrito_list')
    else:
        form = CarritoForm()
    return render(request, 'main/carrito_form.html', {'form': form})

def carrito_update(request, pk):
    carrito = get_object_or_404(Carrito, pk=pk)
    if request.method == 'POST':
        form = CarritoForm(request.POST, instance=carrito)
        if form.is_valid():
            form.save()
            return redirect('carrito_list')
    else:
        form = CarritoForm(instance=carrito)
    return render(request, 'main/carrito_form.html', {'form': form})

def carrito_delete(request, pk):
    carrito = get_object_or_404(Carrito, pk=pk)
    if request.method == 'POST':
        carrito.delete()
        return redirect('carrito_list')
    return render(request, 'main/carrito_confirm_delete.html', {'carrito': carrito})
