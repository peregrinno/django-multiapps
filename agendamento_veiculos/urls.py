from django.urls import path
from django.views.generic import TemplateView
from agendamento_veiculos.views import AgendamentoIndexView, VoltarCore

app_name = 'agendamento_veiculos'

urlpatterns = [
    path('', AgendamentoIndexView.as_view(), name='index_agendamento'),
    path('voltar_core/', VoltarCore.as_view(), name='voltar_core'),
]
