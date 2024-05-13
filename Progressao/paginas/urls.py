from django.urls import path
from django.contrib import admin
from .views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='inicio'),
]