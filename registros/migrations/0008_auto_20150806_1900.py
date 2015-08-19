# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0007_auto_20150806_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen_1',
            field=models.ImageField(default=1, upload_to=b'images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_2',
            field=models.ImageField(default=1, upload_to=b'images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_3',
            field=models.ImageField(default=1, upload_to=b'images'),
            preserve_default=False,
        ),
    ]
