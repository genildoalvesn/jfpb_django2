from django.views.generic.edit import CreateView
from .models import Campo, Atividade
from django.urls import reverse_lazy
class CampoCreate(CreateView):
    model = Campo
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero','pontos','detalhes','campo']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('index')
