# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0013_inventario_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default=1, upload_to=b'images'),
            preserve_default=False,
        ),
    ]
