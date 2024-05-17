from django.urls import path
from django.contrib import admin

from Progressao.paginas.views import PaginaInicial, SobreView, IndexView

urlpatterns = [
    path('modelo/', PaginaInicial.as_view(), name='modelo'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='inicio'),
]