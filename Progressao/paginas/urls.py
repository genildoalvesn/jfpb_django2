from django.urls import path
from django.contrib import admin
from .views import IndexView
from .views import  PaginaInicial
urlpatterns = [
    path('modelo/', PaginaInicial.as_view(), name='modelo'),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='inicio'),
]