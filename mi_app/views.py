from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto
from .forms import BuscarProductoForm


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})
  
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def buscar_producto(request):
    form = BuscarProductoForm()
    resultados = None
    if request.method == 'GET':
        form = BuscarProductoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, 'buscar_producto.html', {'form': form, 'resultados': resultados})
