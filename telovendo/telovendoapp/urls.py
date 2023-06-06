from django.urls import path
from . import views
from .views import lista_usuarios

urlpatterns = [
    path('', views.mensaje, name='telovendo'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
]

