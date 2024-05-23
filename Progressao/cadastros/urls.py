from django.urls import path
from django.contrib import admin

from .views import CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList

from paginas.views import PaginaInicial, SobreView, IndexView

urlpatterns = [

    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name="editar-atividade"),
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade"),
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(),name="excluir-campo"),
    path('list/atividade/', AtividadeList.as_view(), name="list-atividade"),
    path('list/campo/', CampoList.as_view(), name="list-campo"),
    path('cadastrar/campo', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('modelo/', PaginaInicial.as_view(), name="modelo"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="inicio"),


]