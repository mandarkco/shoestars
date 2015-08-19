# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0010_auto_20150812_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_disponible', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad_disponible',
        ),
        migrations.AlterField(
            model_name='tienda',
            name='productos',
            field=models.ManyToManyField(to='registros.Producto', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(to='registros.Producto'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='talla',
            field=models.ForeignKey(to='registros.Talla'),
        ),
    ]
