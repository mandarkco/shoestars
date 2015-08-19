# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=100, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('existencia', models.IntegerField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titular_cuenta_bancaria', models.CharField(max_length=100, null=True, blank=True)),
                ('banco', models.CharField(max_length=50, null=True, blank=True)),
                ('numero_cuenta', models.CharField(max_length=50, null=True, blank=True)),
                ('pais', models.CharField(max_length=50, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('descripcion', models.TextField(max_length=500, null=True, blank=True)),
                ('valor', models.IntegerField(max_length=20, null=True, blank=True)),
                ('peso', models.IntegerField(max_length=20, null=True, blank=True)),
                ('estado', models.BooleanField(default=False)),
                ('privado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(to='services.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=50, null=True, blank=True)),
                ('productos', models.ManyToManyField(to='services.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fuente', models.CharField(max_length=50)),
                ('valor', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('confirmacion_de_pago', models.BooleanField(default=False)),
                ('vendedor', models.ForeignKey(to='services.Perfil')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='tienda',
            field=models.ForeignKey(blank=True, to='services.Tienda', null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='inventario',
            name='categoria',
            field=models.ForeignKey(to='services.Producto'),
        ),
    ]
