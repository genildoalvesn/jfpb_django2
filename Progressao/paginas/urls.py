from django.urls import path
from django.contrib import admin
from .views import IndexView
from .views import  PaginaInicial, SobreView
urlpatterns = [
    path('/', IndexView.as_view(), name='inicio'),
    path('modelo/', PaginaInicial.as_view(), name='modelo'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('admin/', admin.site.urls),

]