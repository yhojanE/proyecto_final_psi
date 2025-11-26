from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.saludo, name="vista"),
    path("principal/", views.primeraVista, name="vistaUno"),
    path("vistaDos/", views.segundaVista, name="vistaDos"),
    path("vistaTres/", views.terceraVista, name="vistaTres"),
    path("vistaCuatro/", views.cuartaVista, name="vistaCuatro"),
    path("quintaCuatro/", views.quintaVista, name="vistaQuinta")
    
]