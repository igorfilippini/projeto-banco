from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .models import ContaBancaria
from .forms import ContaBancariaForm

def lista_contas(request):
    contas = ContaBancaria.objects.all()
    return render(request, 'banco/lista_contas.html', {'contas': contas})

#CREATE 

def criar_conta(request):
    if request.method == 'POST':
        form = ContaBancariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contas')
    else:
        form = ContaBancariaForm()
    return render(request, 'banco/criar_conta.html', {'form': form})

#READ

def consultar_saldo(request, numero_conta):
    conta = ContaBancaria.objects.get(numero_conta=numero_conta)
    return render(request, 'banco/consultar_saldo.html', {'conta': conta})

#UPTADE

def depositar(request, numero_conta):
    conta = get_object_or_404(ContaBancaria, numero_conta=numero_conta)
    if request.method == 'POST':
        valor = Decimal(request.POST.get('valor'))
        conta.saldo += valor
        conta.save()
        return redirect('consultar_saldo', numero_conta=numero_conta)
    return render(request, 'banco/depositar.html', {'conta': conta})


def sacar(request, numero_conta):
    conta = get_object_or_404(ContaBancaria, numero_conta=numero_conta)
    if request.method == 'POST':
        valor = Decimal(request.POST.get('valor'))
        if conta.saldo >= valor:
            conta.saldo -= valor
            conta.save()
            return redirect('consultar_saldo', numero_conta=numero_conta)
        else:
            return render(request, 'banco/sacar.html', {'conta': conta, 'erro': 'Saldo insuficiente.'})
    return render(request, 'banco/sacar.html', {'conta': conta})

#DELETE 

def encerrar_conta(request, numero_conta):
    conta = get_object_or_404(ContaBancaria, numero_conta=numero_conta)
    if request.method == 'POST':
        if conta.saldo == 0:
            conta.delete()
            return redirect('lista_contas')
        else:
            return render(request, 'banco/encerrar_conta.html', {'conta': conta, 'erro': 'Não é possível encerrar uma conta com saldo diferente de zero.'})
    return render(request, 'banco/encerrar_conta.html', {'conta': conta})


