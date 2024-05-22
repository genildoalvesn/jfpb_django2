from django.urls import path
from django.contrib import admin
from .views import CampoCreate, AtividadeCreate
from paginas.views import PaginaInicial, SobreView, IndexView

urlpatterns = [
    path('cadastrar/campo', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('modelo/', PaginaInicial.as_view(), name='modelo'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='inicio'),
]