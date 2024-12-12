from django import forms
from .models import Conta

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ('nome_cliente', 'numero', 'saldo')

class DepositoForm(forms.Form):
    valor = forms.DecimalField(max_digits=10, decimal_places=2)

class SaqueForm(forms.Form):
    valor = forms.DecimalField(max_digits=10, decimal_places=2)

