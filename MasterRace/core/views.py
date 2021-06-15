from core.models import Producto,Fabricante,Componente
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'index.html',contexto)  

def FormAddProd(request):
    fabricantes = Fabricante.objects.all()
    componentes = Componente.objects.all()
    contexto = {'fabricantes': fabricantes, 'componentes': componentes}
    return render(request, 'agregarProducto.html',contexto)

#Administrativo 
def Panel(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request,'panel.html', contexto)

    
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

