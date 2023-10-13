from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppLacasona.models import Avatar, PublicacionDeImagen

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["usuario", "imagen"]


class FormularioDePublicacion(forms.ModelForm):
    class Meta:
        model = PublicacionDeImagen
        fields = ['imagen', 'mensaje']