from django.urls import path
from .views import RedChamados, CoreIndexView, ChooseAppView, RedAgendamentos

app_name = 'core'

urlpatterns = [
    path('', CoreIndexView.as_view(), name='index_core'),
    path('choose_app/', ChooseAppView.as_view(), name='choose_app'),
    path('red_chamados/', RedChamados.as_view(), name='index_chamados'),
    path('red_agendamentos/', RedAgendamentos.as_view(), name='index_agendamento'),
]



