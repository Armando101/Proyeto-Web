# Generated by Django 2.0.4 on 2018-05-13 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Nombre de usuario', max_length=30)),
                ('hora', models.TimeField(help_text='Formato hora:minutos')),
                ('dia', models.DateField(help_text='Formato dia/mes/año')),
                ('email', models.EmailField(help_text='Correo electronico', max_length=254)),
                ('servicio', models.CharField(choices=[('1', 'Manicura permanente'), ('2', 'Tratamientos facial'), ('3', 'Depilación corporal'), ('4', 'Manicura convencional'), ('5', 'Depilación de cejas'), ('6', 'Extensiones de pestañas'), ('7', 'Corte de pelo')], default='1', help_text='Eliga su servicio', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Logeado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Nombre de usuario', max_length=30)),
                ('password', models.CharField(help_text='Contraseña', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Opiniones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(default='', max_length=300)),
                ('terminos', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fechaCreacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaPublicacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idenfificador', models.IntegerField(default=1, help_text='Procure que cada cuarto elemento tenga un identificador multiplo de 4')),
                ('categoria', models.CharField(choices=[('Maquillaje', (('OjosPestañas', 'Ojos y Pestañas'), ('Bases', 'Bases'), ('Sombras', 'Sombras'), ('Labiales', 'Labiales'))), ('Barnices', (('Flora', 'Flora Mini'), ('Escarcha', 'Escarcha Mini'), ('Fuits', 'Fuits Mini'))), ('Cuidado Personal', (('Personal', 'Cuidado Personal'),)), ('Cuidado Cabello', (('Cabello', 'Cuidado del Cabello'),)), ('Perfumes y Lociones', (('Perfumes', 'Perfumes'), ('Lociones', 'Lociones')))], default='1', max_length=25)),
                ('nombre', models.CharField(max_length=120)),
                ('nota', models.CharField(max_length=120)),
                ('descripcion', models.CharField(default='', max_length=300)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('peso', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('imagen', models.CharField(max_length=120)),
                ('existencias', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Recuperacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Correo electronico', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(help_text='Nombre de usuario', max_length=30, primary_key=True, serialize=False)),
                ('password1', models.CharField(help_text='Contraseña', max_length=30)),
                ('password2', models.CharField(help_text='Confirmacion de contraseña', max_length=30)),
                ('first_name', models.CharField(help_text='Nombre', max_length=30)),
                ('last_name', models.CharField(help_text='Apellido', max_length=30)),
                ('email', models.EmailField(help_text='Correo electronico', max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
