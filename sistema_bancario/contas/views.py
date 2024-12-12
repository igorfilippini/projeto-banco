from django.shortcuts import render, redirect
from .models import Conta
from .forms import ContaForm, DepositoForm, SaqueForm

def criar_conta(request):
    if request.method == 'POST':
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contas')
    else:
        form = ContaForm()
    return render(request, 'contas/criar_conta.html', {'form': form})

def lista_contas(request):
    contas = Conta.objects.all()
    return render(request, 'contas/lista_contas.html', {'contas': contas})

def consultar_saldo(request, pk):
    conta = Conta.objects.get(pk=pk)
    return render(request, 'contas/consultar_saldo.html', {'conta': conta})

def depositar(request, pk):
    conta = Conta.objects.get(pk=pk)
    if request.method == 'POST':
        form = DepositoForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            conta.saldo += valor
            conta.save()
            return redirect('consultar_saldo', pk=pk)
    else:
        form = DepositoForm()
    return render(request, 'contas/depositar.html', {'form': form, 'conta': conta})

def sacar(request, pk):
    conta = Conta.objects.get(pk=pk)
    if request.method == 'POST':
        form = SaqueForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            if conta.saldo >= valor:
                conta.saldo -= valor
                conta.save()
                return redirect('consultar_saldo', pk=pk)
            else:
                return render(request, 'contas/saldo_insuficiente.html')
    else:
        form = SaqueForm()
    return render(request, 'contas/sacar.html', {'form': form, 'conta': conta})

def encerrar_conta(request, pk):
    conta = Conta.objects.get(pk=pk)
    if conta.saldo == 0:
        conta.delete()
        return redirect('lista_contas')
    else:
        return render(request, 'contas/conta_nao_encerrada.html')

