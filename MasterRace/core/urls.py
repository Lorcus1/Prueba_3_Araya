from core.models import Producto
from django.contrib import admin
from django.urls import path, include
from core.views import index, Producto, FormAddProd, Panel, SignIn, In, Out, SignUp, CreateUser

urlpatterns = [
    path('',index, name='index'),

    path('panel/', Panel, name='Panel'),
    path('panel/formadd',FormAddProd, name='FormAddProd'),


    path('signin/', SignIn, name='SignIn'),
    path('signin/in/', In, name='In'),
    path('signin/out/', Out, name='Out'),

    path('signup/', SignUp, name='SignUp'),
     path('signup/createuser', CreateUser, name='CreateUser'),

]
