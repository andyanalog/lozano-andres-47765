from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import FormularioDePublicacion
from django.contrib.auth import login as auth_login, authenticate
from AppLacasona.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def login(request):

    form = AuthenticationForm(request, data=request.POST)
    
    if request.method == "POST" and form.is_valid():
        usuario = form.cleaned_data.get("username")
        contra = form.cleaned_data.get("password")

        user = authenticate(request, username=usuario, password=contra)

        if user:
            auth_login(request, user)
            return render(request, "AppLacasona/inicio2.html", {"mensaje": f"Bienvenido, {user}"})
        else:
            return render(request, "AppLacasona/inicio.html", {"mensaje": "Datos incorrectos."})
    
    return render(request, "AppLacasona/login.html", {"formulario": form})

def logout_view(request):
    logout(request)
    return redirect("AppLacasona/inicio.html")

def register(request):
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppLacasona/inicio.html", {"mensaje": "Usuario creado."})
    else:
        form = UsuarioRegistro()
    
    return render(request, "AppLacasona/register.html", {"formulario": form})


    
def inicio(request):
    return render(request,"AppLacasona/inicio.html")

def inicio2(request):
    return render(request,"AppLacasona/inicio2.html")

def newsletter(request):

#    if request.method == 'POST':
#        nuevomailfornl = Newsletter(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
#        nuevomailfornl.save()
#        return render(request,"AppLacasona/inicio.html")    
    return render(request, "AppLacasona/see_newsletter.html")

def sendsong(request):
    return render(request,"AppLacasona/see_sendsong.html")

def askanything(request):
    return render(request,"AppLacasona/see_askanything.html")

def aboutme(request):
    return render(request, "AppLacasona/see_aboutme.html")


    #vista para subir imagenes
@login_required
def agregarImagen(request):

    if request.method == "POST":

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            avatar = Avatar(usuario=request.user, imagen=informacion["imagen"])
            avatar.save()
            return render(request, "AppLacasona/inicio.html")
    else:

            miFormulario = AvatarFormulario()

    return render(request,"AppLacasona/agregarimg.html", {"form":miFormulario})

@login_required
def form_mailfornl(request):
    if request.method == 'POST':
        nuevomailfornl = Newsletter(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
        nuevomailfornl.save()
        return render(request,"AppLacasona/inicio.html")
    
    return render(request, "AppLacasona/form_newsletter.html", {'usuario_autenticado': True})

@login_required
def form_sendsong(request):
    if request.method == 'POST':
        nuevoformsong = SendSong(songname=request.POST["songname"], email=request.POST["email"], url=request.POST["url"])
        nuevoformsong.save()
        return render(request,"AppLacasona/inicio.html")
    
    return render(request, "AppLacasona/form_sendsong.html", {'usuario_autenticado': True})

@login_required
def form_askanything(request):
    if request.method == 'POST':
        nuevoformask = AskAnything(message=request.POST["message"], email=request.POST["email"])
        nuevoformask.save()
        return render(request,"AppLacasona/inicio.html")
    
    return render(request, "AppLacasona/form_askanything.html", {'usuario_autenticado': True})

@login_required
def form_postpic(request):
    if request.method == 'POST':
        formulario = FormularioDePublicacion(request.POST, request.FILES)
        if formulario.is_valid():
            imagen = formulario.save()  
            return redirect('pagina_de_imagen', imagen_id=imagen.id)  # redirige a la página de imagen
    else:
        formulario = FormularioDePublicacion()

    return render(request, 'AppLacasona/form_postpic.html', {'formulario': formulario})

def search_mailfornl(request):
    return render(request, "AppLacasona/search_mailfornl.html")


def view_mailfornl(request):

    if request.GET["email"]:

        email = request.GET["email"]
        all_emails = Newsletter.objects.filter(email__icontains=email)

        return render(request, "AppLacasona/view_mailfornl.html", {"all_emails": all_emails, "email":email})
    
    else:

        respuesta = "No estas suscrito al Newsletter."

    return HttpResponse(respuesta)

def pagina_de_imagen(request, imagen_id):
    imagen = get_object_or_404(PublicacionDeImagen, id=imagen_id)
    return render(request, 'AppLacasona/pagina_de_imagen.html', {'imagen': imagen})

def view_postpic(request):
    imagenes = PublicacionDeImagen.objects.all()
    return render(request, 'AppLacasona/view_postpic.html', {'imagenes': imagenes})





















"""""
def email_nl(request):
    emailnl = Newsletter(nombre="andres", apellido="lozano", email="andyxinvierno@gmail.com")
    emailnl.save()
    return HttpResponse(f"Te enviaremos información a {emailnl.email}")

def song_request(request):
    songrequest = SendSong(songname="Adios", deadline=20/20/2020)
    songrequest.save()
    return HttpResponse(f"Haz enviado tu canción {songrequest.songname}. Te enviaremos informacion de cuanto sale masterizarla antes de tu deadline {songrequest.deadline}")
"""""