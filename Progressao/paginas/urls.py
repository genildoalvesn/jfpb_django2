from django.urls import path
from django.contrib import admin
from .views import IndexView
from .views import PaginaInicial, SobreView, CampoInicioView,  CadastroInicioView


urlpatterns = [
    path('modelo/', PaginaInicial.as_view(), name='modelo'),
    path('cadastroinicio/', CadastroInicioView.as_view(), name='cadastro-inicio'),
    path('campoinicio/', CampoInicioView.as_view(), name='campo-Inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(), name='inicio'),
]