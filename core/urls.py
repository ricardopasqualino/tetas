
from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include
from delivery.views import ( 
    Home, 
    Casa, 
    Morador, 
    Nova, 
    Entrega_nova, 
    Entregas, 
    Login_view, 
    Logout_view, 
    Password_reset, 
    Register, 
    Atualizar_entrega,
    Erro,   
)

urlpatterns = [
    #admin Django
    path('admin/', admin.site.urls, name='Admin'),
    
    #App
    path('', Home, name='Home'),
    path('casa/', Casa, name='Casa'),
    path('morador/', Morador, name='Morador'),
    path('nova/', Nova , name='Nova'),
    path('entrega-nova/', Entrega_nova , name='Entrega_nova'),
    path('atualizar-entrega-<id>/', Atualizar_entrega , name='Atualizar_entrega'),
    path('entregas/', Entregas , name='Entregas'),
    path('erro/', Erro , name='Erro'),
    
    #Autentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', Login_view , name='Login'),
    path('logout/', Logout_view , name='Logout'),
    path('reset-senha/', Password_reset , name='Password_reset'),
    path('cadastro/', Register , name='Register'),
    
    #Email
    path('email/', include('enviaemail.urls')),
]