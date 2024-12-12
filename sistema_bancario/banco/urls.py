
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contas, name='lista_contas'),  # Certifique-se de que este nome está correto
    path('criar/', views.criar_conta, name='criar_conta'),
    path('conta/<str:numero_conta>/', views.consultar_saldo, name='consultar_saldo'),
    path('conta/<str:numero_conta>/deposito/', views.depositar, name='depositar'),
    path('conta/<str:numero_conta>/saque/', views.sacar, name='sacar'),
    path('conta/<str:numero_conta>/encerrar/', views.encerrar_conta, name='encerrar_conta'),
]
