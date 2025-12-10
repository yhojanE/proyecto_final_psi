from django.shortcuts import render
from django.http import HttpResponse

from .models import Practica
from django.shortcuts import render, redirect

def formulario(request):
    if request.method == "POST":
        usern = request.POST.get("username")
        passw1 = request.POST.get("password1")
        passw2 = request.POST.get("password2")
        img_url = request.POST.get("imagen_url")  # <--- AÑADIDO

        if Practica.objects.filter(username=usern).exists():
            sms = "El nombre de usuario ya existe"
            sms2 = "Segundo mensaje"
            info = {
                'infosms': sms,
                'infosms2': sms2
            }
            return render(request, "formulario.html", info)

        if passw1 == passw2:
            Practica.objects.create(
                username=usern,
                password=passw2,
                imagen_url=img_url  # <--- AÑADIDO
            )
            return redirect("login")
    return render(request, "formulario.html")


# Create your views here.
def saludo(request):
    return HttpResponse("Hola mundo")

def primeraVista(request):
    return render(request, 'index.html')

def segundaVista(request):
    return render(request, 'index2.html')

def terceraVista(request):
    return render(request, 'index3.html')

def cuartaVista(request):
    return render(request, 'index4.html')

def quintaVista(request):
    return render(request, 'index5.html')

def login(request):
    return render(request, 'login.html')


# ---------------------------------------------------------
# 👇 NUEVAS VISTAS AÑADIDAS (sin alterar tu código anterior)
# ---------------------------------------------------------

def lista_usuarios(request):

    # verifica si hay sesión activa
    if "usuario_id" not in request.session:
        return redirect("login")

    usuarios = Practica.objects.all()
    return render(request, "lista_usuarios.html", {"usuarios": usuarios})


def eliminar_usuario(request, user_id):
    usuario = Practica.objects.get(id=user_id)
    usuario.delete()
    return redirect("lista_usuarios")


# LOGIN
def login(request):
    mensaje = ""

    if request.method == "POST":
        usuario = request.POST.get("username")
        clave = request.POST.get("password")

        # Buscar el usuario en tu modelo Practica
        try:
            user = Practica.objects.get(username=usuario)
            if user.password == clave:
                # Guardar sesión manual
                request.session["usuario_id"] = user.id
                request.session["usuario_nombre"] = user.username
                return redirect("lista_usuarios")   # Ir a la lista de usuarios
            else:
                mensaje = "Contraseña incorrecta"
        except Practica.DoesNotExist:
            mensaje = "El usuario no existe"

    return render(request, "login.html", {"mensaje": mensaje})


# ---------------------------------------------------------
# 🔥 NUEVA VISTA: EDITAR USUARIO (sin alterar tu código anterior)
# ---------------------------------------------------------

def editar_usuario(request, user_id):
    usuario = Practica.objects.get(id=user_id)

    if request.method == "POST":
        usuario.username = request.POST.get("username")
        usuario.password = request.POST.get("password")
        usuario.imagen_url = request.POST.get("imagen_url")
        usuario.save()

        return redirect("lista_usuarios")

    return render(request, "editar_usuario.html", {"usuario": usuario})
