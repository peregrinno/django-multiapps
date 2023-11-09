from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View

class VoltarCore(View):
    def get(self, *args, **kwargs):
        return redirect('core:CoreIndexView')

# Create your views here.
class ChamadoIndexView(TemplateView):
    template_name = "index_chamados.html"

