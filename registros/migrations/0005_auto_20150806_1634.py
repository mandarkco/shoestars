# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_auto_20150806_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cantidad',
            new_name='disponibles',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='privado',
        ),
        migrations.AlterField(
            model_name='producto',
            name='peso',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
