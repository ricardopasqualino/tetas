from random import random
from django.shortcuts import render, redirect
from core.form import NovaForm, DeliveryForm
from .models import Delivery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


@login_required
def Morador(request):
    return render (request, 'morador.html')


@login_required
def Home(request):
    return render(request, 'index.html')


@login_required
def Nova(request):
    form = NovaForm()
    return render(request, 'nova.html', {'form': form})


@login_required
def Entrega_nova(request):
    form = NovaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Entregas')
    else:
        return redirect('Entregas')

@login_required
def Entregas(request):
    entregas = Delivery.objects.order_by('-data_entrada').all()
    return render(request, 'entregas.html', {'entregas': entregas})


@login_required
def Atualizar_entrega(request, id):
    data = {}
    entrega = Delivery.objects.get(id=id)
    form = DeliveryForm(request.POST or None, instance=entrega)
    data['entrega'] = entrega
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Entregas')
    else:
        return render (request, 'atualizar_entrega.html', data)


@login_required
def Box(request):
    return render (request, 'box.html')


@login_required
def Casa(request):
    return render(request, 'casas.html')


def Login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('Home')
    else:
        return redirect('Home')


def Logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


@login_required
def Password_reset(request):
    return render(request, 'accounts/password_reset.html')


@login_required
def Register(request):
    return render(request, 'accounts/register.html')


def Erro(request):
    return render(request, 'erro.html')


def random_id():
    return str (random.randint(10000, 99999))
