from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages, sessions
from cuerpo.models import Post, User
from cuerpo.forms import PostFormulario, SignUpForm, LoginForm, CitasForm

# Create your views here. Ba

def index(request):
    return render(request, 'cuerpo/index.html', {})

def productos(request):
    return render(request, 'cuerpo/productos.html', {})

def opiniones(request):
    return render(request, 'cuerpo/opiniones.html', {})

def contacto(request):
    return render(request, 'cuerpo/contacto.html', {})

def tips(request):
    return render(request, 'cuerpo/tips.html', {})

def cerrar(request):
        request.session['USUARIO_LOGEADO'] = ""
        messages.info(request, 'Se ha cerrado la sesion')
        return redirect('login')

def login(request):
    USUARIO_LOGEADO = request.session.get('USUARIO_LOGEADO')
    if not USUARIO_LOGEADO:
        request.session['USUARIO_LOGEADO'] = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.password = form.cleaned_data.get('password')
            usuario = User.objects.get(username=user.username)
            if(USUARIO_LOGEADO != ""):
                messages.info(request, 'Usuario ya esta logeado')
            elif(user.password != usuario.password1):
                messages.info(request, 'Informacion erronea')
            else:
                request.session['USUARIO_LOGEADO'] = user.username
                messages.info(request, 'Bienvenid@ ' + user.username)
                return render(request, 'cuerpo/index.html', {})
    else:
        form = LoginForm()
    return render(request, 'cuerpo/login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            if(user.password1 != user.password2):
                messages.info(request, 'Contraseñas no concuerdan.')
            else:
                user.save()
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'cuerpo/registro.html', {'form': form})

def citas(request):
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            if(user.password1 != user.password2):
                messages.info(request, 'Contraseñas no concuerdan.')
            else:
                user.save()
                return redirect('index')
    else:
        form = CitasForm()
    return render(request, 'cuerpo/citas.html', {'form': form})

def listadoPosts(request):
    posts = Post.objects.filter(fechaPublicacion__lte = timezone.now()).order_by('fechaPublicacion')
    return render(request,'cuerpo/listadoPosts.html',{'posts':posts})

def detalles(request, pk):
    posts = get_object_or_404(Post, pk = pk)
    return render(request, 'cuerpo/detalles.html', {'post': posts})

def nuevoPost(request):
    if request.method == 'POST':
        form = PostFormulario(request.POST)
        if  form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fechaPublicacion = timezone.now()
            post.save()
            return redirect('detalles',pk=post.pk)
    else:
        form = PostFormulario()
    return render(request, 'cuerpo/editar.html',{'form':form})

def modificar(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostFormulario(request.POST,instance=post)
        if  form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalles',pk=post.pk)
    else:
        form = PostFormulario(instance=post)
    return render(request, 'cuerpo/editar.html',{'form':form})