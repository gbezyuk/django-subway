# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('color', colorful.fields.RGBColorField(verbose_name='color', colors=('#FF0000', '#0070BB', '#009245', '#FBA820', '#662C91'))),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'subway branch',
                'abstract': False,
                'verbose_name_plural': 'subway branches',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('branch', models.ForeignKey(verbose_name='branch', to='subway.Branch')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'subway station',
                'abstract': False,
                'verbose_name_plural': 'subway stations',
            },
        ),
    ]
