# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_auto_20150806_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='disponibles',
            new_name='cantidad_disponible',
        ),
    ]
