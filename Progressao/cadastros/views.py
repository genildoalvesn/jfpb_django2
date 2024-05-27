from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, Atividade
from django.urls import reverse_lazy
# Create your views here.
class CampoCreate(CreateView):
    model = Campo
    fields = ['name', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero','descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

#################  UPDATE ####################

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao','pontos','detalhes','campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    ################### Delete ##################################
class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('index')

##################### List #######################################
class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'
