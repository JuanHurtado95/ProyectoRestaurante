from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from gestionPedidos.models import ingredientes
from django.views.generic import TemplateView
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, "home1.html")

"""class home(TemplateView):
    template_name='home1.html'"""


def busqueda_ingredientes(request):
     
    return render(request, "busqueda_ingredientes.html")


def buscar(request):

    if request.GET["prd"]:
        
        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]

        if len(producto)>20:

            mensaje="El texto es demaciado largo"
        
        else:

            articulos=ingredientes.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})

    else:
        mensaje="Busqueda erronea"

    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":
        return render(request, "gracias.html")
    
    return render(request, "contacto.html")

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm() 
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def registroUser(request):

    return render(request, "registerUser.html")

def loginUser(request):

    return render(request, "loginUser.html")

"""class loginUser(TemplateView):
    template_name='loginUser.html'"""

def menu(request):

    return render(request, "menu.html")