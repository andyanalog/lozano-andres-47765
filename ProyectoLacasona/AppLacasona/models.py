from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Newsletter(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class SendSong(models.Model):
    songname = models.CharField(max_length=30)
    email = models.EmailField(default="correo@ejemplo.com")
    url = models.URLField(default="https://ejemplo.com")
#    deadline = models.DateField()

class AskAnything(models.Model):
    message = models.CharField(max_length=100)
    email = models.EmailField(default="correo@ejemplo.com")

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class PublicacionDeImagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes/')
    mensaje = models.TextField()