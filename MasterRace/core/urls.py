from core.models import Producto
from django.contrib import admin
from django.urls import path, include
from core.views import index, FormAddProd, Panel, SignIn, In, Out, SignUp, CreateUser, Add, FormModProd, Mod,Del,Prod

urlpatterns = [
    path('',index, name='index'),

    path('panel/', Panel, name='Panel'),

    path('panel/formadd',FormAddProd, name='FormAddProd'),
    path('panel/formadd/add',Add, name='Add'),

    path('formmod/<int:ID>', FormModProd, name='FormModProd'),
    path('mod/<int:ID>', Mod, name='Mod'),

    path('panel/del/<int:ID>', Del, name='Del'),

    path('prod/<int:ID>',Prod, name='Prod'),

    path('signin/', SignIn, name='SignIn'),
    path('signin/in/', In, name='In'),
    path('signin/out/', Out, name='Out'),

    path('signup/', SignUp, name='SignUp'),
    path('signup/createuser', CreateUser, name='CreateUser'),

]
