# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0011_auto_20150813_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talla',
            name='numero',
            field=models.CharField(max_length=50),
        ),
    ]
