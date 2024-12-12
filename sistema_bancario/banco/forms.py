from django import forms
from .models import ContaBancaria

class ContaBancariaForm(forms.ModelForm):
    class Meta:
        model = ContaBancaria
        fields = ['nome', 'numero_conta', 'saldo']
