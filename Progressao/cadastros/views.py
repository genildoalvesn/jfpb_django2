from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, Atividade
from django.urls import reverse_lazy
# Create your views here.
class CampoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['name', 'descricao']
    template_name = 'cadastros/cadastrar.html'
    success_url = reverse_lazy('list-campo')
class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero','descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/cadastrar.html'
    success_url = reverse_lazy('list-atividade')

#################  UPDATE ####################

class CampoUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome','descricao']
    template_name = 'cadastros/cadastrar.html'
    success_url = reverse_lazy('list-campo')
class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao','pontos','detalhes','campo']
    template_name = 'cadastros/cadastrar.html'
    success_url = reverse_lazy('list-atividade')
    ################### Delete ##################################
class CampoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('list-campo')
class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('list-atividade')

##################### List #######################################
class CampoList(LoginRequiredMixin,ListView):

    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/listar-campo.html'

class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/listar-atividade.html'

class PaginaInicial(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'modelo.html'

class SobreView(TemplateView):
    template_name ='sobre.html'

class IndexView(TemplateView):
    template_name = 'index.html'