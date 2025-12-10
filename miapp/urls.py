from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.saludo, name="vista"),
    path("principal/", views.primeraVista, name="vistaUno"),
    path("vistaDos/", views.segundaVista, name="vistaDos"),
    path("vistaTres/", views.terceraVista, name="vistaTres"),
    path("vistaCuatro/", views.cuartaVista, name="vistaCuatro"),
    path("quintaCuatro/", views.quintaVista, name="vistaQuinta"),
    path("formulario/", views.formulario, name="formulario"),
    path("login/", views.login, name="login"),

    # 👇 Rutas añadidas sin alterar tu código existente
    path("usuarios/", views.lista_usuarios, name="lista_usuarios"),
    path("usuarios/eliminar/<int:user_id>/", views.eliminar_usuario, name="eliminar_usuario"),

    # 🔥 NUEVA RUTA PARA ACTUALIZAR USUARIO
    path("usuarios/editar/<int:user_id>/", views.editar_usuario, name="editar_usuario"),
]
