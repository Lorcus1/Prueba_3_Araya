from core.models import Producto,Fabricante,Componente
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#Index
def index(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'index.html',contexto)  


#Administrativo 
def Panel(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request,'panel.html', contexto)

#Agregar Producto
def FormAddProd(request):
    fabricantes = Fabricante.objects.all()
    componentes = Componente.objects.all()
    contexto = {'fabricantes': fabricantes, 'componentes': componentes}
    return render(request, 'agregarProducto.html',contexto)

def Add(request):
    ID              = request.POST.get('ID','')
    Nombre          = request.POST.get('Nombre','')
    id_Fabricante   = request.POST.get('Fabricante','')
    id_Componente   = request.POST.get('Componente','')
    Precio          = request.POST.get('Precio','')
    Stock           = request.POST.get('Stock','')
    Imagen          = request.FILES.get('Imagen','')

    fabricante = Fabricante.objects.get(ID=id_Fabricante)
    componente = Componente.objects.get(ID=id_Componente)

    producto = Producto(Nombre=Nombre,Fabricante=fabricante,Componente=componente,Precio=Precio,Stock=Stock, Imagen=Imagen)
    producto.save()
    return redirect('Panel')

#Modificar Producto
def FormModProd(request, ID):
    producto =Producto.objects.get(ID = ID)
    fabricantes = Fabricante.objects.all()
    componentes = Componente.objects.all()
    contexto = {'producto': producto , 'fabricantes' : fabricantes, 'componentes' : componentes}

    return render(request, 'modificarProducto.html',contexto)

def Mod(request, ID):
    
    Nombre          = request.POST.get('Nombre','')
    id_Fabricante   = request.POST.get('Fabricante','')
    fabricante      = Fabricante.objects.get(ID=id_Fabricante)

    id_Componente   = request.POST.get('Componente','')
    componente      = Componente.objects.get(ID=id_Componente)
    
    Precio          = request.POST.get('Precio','')
    Stock           = request.POST.get('Stock','')
    Imagen          = request.FILES.get('Imagen')

    producto = Producto.objects.get(ID = ID)
    producto.Nombre = Nombre
    producto.Fabricante = fabricante
    producto.Componente = componente
    producto.Precio = Precio
    producto.Stock = Stock
    print(Imagen)
        
    if(Imagen!=''):
        producto.Imagen = Imagen

    producto.save()
    
    return redirect('Panel')

def Del (request, ID):
    producto = Producto.objects.get(ID=ID)
    producto.delete()
    return redirect('Panel')
    
#Login
def SignIn(request):
    contexto={}
    return render(request,'signin.html',contexto)

def In(request):
    username = request.POST.get('usuario','default')
    password = request.POST.get('clave','default')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        
        return redirect('index')
    else:
        return redirect(SignIn)

def Out(request):
    logout(request)
    return redirect ('index')



#Register

def SignUp(request):
    contexto={}
    return render(request,'signup.html',contexto)

def CreateUser(request):
    contexto={}
    username = request.POST.get('usuario','default')
    email = request.POST.get('email','default')
    password = request.POST.get('clave','default')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return redirect('SignUp')
    else:
        user = User.objects.create_user(username, email, password)
        return redirect('index')
        user.save()
    return render(request,'signin.html')

