# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20150720_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(default=1, to='services.Producto'),
            preserve_default=False,
        ),
    ]
