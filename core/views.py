from django.shortcuts import redirect
from django.views.generic import TemplateView

# Create your views here.
class CoreIndexView(TemplateView):
    template_name = "index_core.html"
    
class CoreLogoutView(TemplateView):
    template_name = "index_core.html"

class ChooseAppView(TemplateView):
    template_name = "choose_app.html"

class RedChamados(TemplateView):
    template_name = 'index_chamados.html'

    def dispatch(self, *args, **kwargs):
        return redirect('chamados:ChamadoIndexView')
    
class RedAgendamentos(TemplateView):
    template_name = 'index_agendamento.html'

    def dispatch(self, *args, **kwargs):
        return redirect('agendamento_veiculos:AgendamentoIndexView')


        

