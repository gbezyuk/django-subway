# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immovables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishingType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
            ],
            options={
                'verbose_name': 'finishing type',
                'verbose_name_plural': 'finishing types',
            },
        ),
        migrations.RemoveField(
            model_name='assignation',
            name='square',
        ),
        migrations.AddField(
            model_name='assignation',
            name='elevator_available',
            field=models.BooleanField(verbose_name='elevator available', default=True),
        ),
        migrations.AddField(
            model_name='assignation',
            name='floor',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='floor'),
        ),
        migrations.AddField(
            model_name='assignation',
            name='floors_total',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='floors total'),
        ),
        migrations.AddField(
            model_name='assignation',
            name='kitchen_area',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='living area'),
        ),
        migrations.AddField(
            model_name='assignation',
            name='living_area',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='living area'),
        ),
        migrations.AddField(
            model_name='assignation',
            name='total_area',
            field=models.PositiveIntegerField(verbose_name='total area', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignation',
            name='finishing_type',
            field=models.ForeignKey(blank=True, null=True, verbose_name='finishing type', to='immovables.FinishingType'),
        ),
    ]
