from django.urls import path
from chamados.views import ChamadoIndexView, VoltarCore

app_name = 'chamados'

urlpatterns = [
    path('', ChamadoIndexView.as_view(), name='index_chamados'),
    path('voltar_core/', VoltarCore.as_view(), name='voltar_core'),
]
