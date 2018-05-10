from django import forms
from .models import Post, User, Logeado, HacerCita
from .choices import *

SERVICES_CHOICES = (
    ('1', 'Masaje'),
    ('2', 'Facial'),
    ('3', 'Uñas')
)

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'texto')

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        labels = {
            'username' : "Nombre de usuario",
            'first_name': "Nombre(s)",
            'last_name': "Apellido(s)",
            'email': "Correo electronico",
            'password1': "Contraseña",
            'password2': "Confirmacion de contraseña",
        }
        widgets = {
            'password2' : forms.PasswordInput(),
            'password1' : forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Logeado
        fields = ('username', 'password')
        labels = {
            'username': "Nombre de usuario",
            'password': "Contraseña",
        }
        widgets = {
            'password' : forms.PasswordInput()
        }

class CitasForm(forms.ModelForm):
    #servicio = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=SERVICES_CHOICES)
    CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)
    servicio = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = HacerCita
        fields = ('username', 'dia', 'hora', 'email',)
