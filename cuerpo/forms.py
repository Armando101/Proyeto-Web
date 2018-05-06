from django import forms
from .models import Post, User, Logeado

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'texto')

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'password2' : forms.PasswordInput(),
            'password1' : forms.PasswordInput()
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Logeado
        fields = ('username', 'password')
        widgets = {
            'password' : forms.PasswordInput()
        }