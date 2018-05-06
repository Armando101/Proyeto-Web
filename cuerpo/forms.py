from django import forms
from .models import Post, Usuario

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'texto')


class FormularioRegistroUno(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'password',)