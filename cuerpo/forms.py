from django import forms
from .models import Post, User

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'texto')

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(max_length=30, help_text='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, help_text='Confirmacion de contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
