# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_producto_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='valor',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Inventario',
        ),
    ]
