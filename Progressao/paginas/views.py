from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
class PaginaInicial(TemplateView):
    template_name = 'modelo.html'
class CampoInicioView(TemplateView):
    template_name ='campoinicio.html'

class CadastroInicioView(TemplateView):
    template_name = 'cadastroinicio.html'

class SobreView(TemplateView):
    template_name ='sobre.html'