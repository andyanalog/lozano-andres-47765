from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from AppLacasona import views

urlpatterns = [

    #url inicio
    path("inicio/", inicio, name="Inicio"),
    path("inicio2/", inicio2, name="Inicio2"),

    #urls leer
    path("newsletter/", newsletter, name="Newsletter"),
    path("sendsong/", sendsong, name="Sendsong"),
    path("askanything/", askanything, name="Askanything"),
    path("aboutme/", aboutme, name="AboutMe"),
    path("login/", login, name="Login"),
    path("register/", register, name="Register"),
    path("logut/", LogoutView.as_view(template_name="AppLacasona/logout.html"), name="Logout"),
    path("view_postpic/", form_postpic, name="ViewPostpic"),

    #urls de formularios
    path("form_newsletter/", form_mailfornl, name="FormNewsletter"),
    path("form_sendsong/", form_sendsong, name="FormSendSong"),
    path("form_askanything/", form_askanything, name="FormAskAnything"),
    path('form_postpic/', views.form_postpic, name='FormPostpic'),


    #urls de búsqueda
    path("search_mailfornl/", search_mailfornl, name="SearchMailfornl"),
#    path("view_mailfornl/", view_mailfornl, name="ViewMailfornl"),
    path("agregarimg/", views.agregarImagen, name="Subir Avatar"),
]