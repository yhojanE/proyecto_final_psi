from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo (request):
    return HttpResponse("Hola mundo")
def primeraVista (request):
    return render(request, 'index.html')
def segundaVista (request):
    return render(request, 'index2.html')
def terceraVista (request):
    return render(request, 'index3.html')
def cuartaVista (request):
    return render(request, 'index4.html')
def quintaVista (request):
    return render(request, 'index5.html')



