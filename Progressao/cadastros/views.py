from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Progressao
from .models import Campo, Atividade
from django.urls import reverse_lazy
# Create your views here.
class CampoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['name', 'descricao']
    template_name = 'cadastros/cadastrar.html'
    success_url = reverse_lazy('list-campo')
class AtividadeCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
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
class AtividadeUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
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
class AtividadeDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('list-atividade')

##################### List #######################################
class CampoList(LoginRequiredMixin,ListView):

    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/listar-campo.html'

class AtividadeList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/listar-atividade.html'

class PaginaInicial(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'modelo.html'

class SobreView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name ='sobre.html'

class ProgressaoCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Progressao
    fields = ['classe ' , 'data_inicial', 'data_final' , 'observação']
    template_name ='cadastros/form.html'
    success_url = reverse_lazy ('listar-atividade')

    def form_valid(self,form):

        # antes do super não foi criado o objeto nem salvo no banco
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # Depois do super o objeto esta criado
        return url

class IndexView(TemplateView):
        template_name = 'index.html'