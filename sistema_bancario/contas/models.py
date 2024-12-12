from django.db import models

class Conta(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nome_cliente = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conta {self.numero} - {self.nome_cliente}"
