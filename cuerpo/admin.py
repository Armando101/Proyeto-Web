from django.contrib import admin
from .models import Post, User, Cita, Opiniones, Producto

# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Cita)
admin.site.register(Opiniones)
admin.site.register(Producto)
