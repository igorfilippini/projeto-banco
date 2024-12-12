from django.db import models

class ContaBancaria(models.Model):
    nome = models.CharField(max_length=100)
    numero_conta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.numero_conta}"
