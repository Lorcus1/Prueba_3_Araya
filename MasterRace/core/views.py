from core.models import Producto,Fabricante,Componente
from django.shortcuts import render, redirect

def index(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'index.html',contexto)  
    

def agregarProducto(request):
    fabricantes = Fabricante.objects.all()
    componentes = Componente.objects.all()
    contexto = {'fabricantes': fabricantes, 'componentes': componentes}
    ID = request.POST.get('ID','')

  

