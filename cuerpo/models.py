from django.db import models
from django.utils import timezone

# Create your models here. Va

class Post(models.Model):
    """
    Modelo para almacenar los posts
    """
    autor = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    titulo = models.CharField(max_length= 200)
    texto = models.TextField()
    fechaCreacion = models.DateTimeField(
        default = timezone.now
    )
    fechaPublicacion = models.DateTimeField(
        blank= True, null = True
    )

    def publicar(self):
        """
        Método para obtener la fecha de publicación
        cuando se publique algún Post
        """
        self.fechaPublicacion = timezone.now()
        self.save()

    #Método mágico que nos permite castear un objeto a una cadena
    def __str__(self):
        return self.titulo


class User(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario', primary_key=True)
    password1 = models.CharField(max_length=30, help_text='Contraseña')
    password2 = models.CharField(max_length=30, help_text='Confirmacion de contraseña')
    first_name = models.CharField(max_length=30, help_text='Nombre')
    last_name = models.CharField(max_length=30, help_text='Apellido')
    email = models.EmailField(max_length=254, help_text='Correo electronico')

    def __str__(self):
        return self.username


class Logeado(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario')
    password = models.CharField(max_length=30, help_text='Contraseña')

    def __str__(self):
        return self.username
