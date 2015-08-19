# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='fuente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='valor',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='vendedor',
        ),
        migrations.AddField(
            model_name='venta',
            name='tienda',
            field=models.ForeignKey(default=1, to='services.Tienda'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(to='services.Cliente'),
        ),
    ]
