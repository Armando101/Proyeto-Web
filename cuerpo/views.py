from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .models import Post
from .forms import PostFormulario

# Create your views here. Ba

def index(request):
    return render(request, 'cuerpo/index.html', {})

def productos(request):
    return render(request, 'cuerpo/productos.html', {})

def opiniones(request):
    return render(request, 'cuerpo/opiniones.html', {})

def contacto(request):
    return render(request, 'cuerpo/contacto.html', {})

def login(request):
    return render(request, 'cuerpo/login.html', {})

def registroinicial(request):
    return render(request, 'cuerpo/registroinicial.html', {})

def registroformal(request):
    return render(request, 'cuerpo/registroformal.html', {})

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