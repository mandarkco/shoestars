# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_venta_talla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='tienda',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='tienda',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Inventario',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Tienda',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]
