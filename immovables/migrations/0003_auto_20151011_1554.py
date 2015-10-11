# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.shared.fields


class Migration(migrations.Migration):

    dependencies = [
        ('immovables', '0002_auto_20151011_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignation',
            name='kitchen_area',
            field=core.shared.fields.PositiveDecimalField(max_digits=10, null=True, decimal_places=2, blank=True, verbose_name='living area'),
        ),
        migrations.AlterField(
            model_name='assignation',
            name='living_area',
            field=core.shared.fields.PositiveDecimalField(max_digits=10, null=True, decimal_places=2, blank=True, verbose_name='living area'),
        ),
        migrations.AlterField(
            model_name='assignation',
            name='total_area',
            field=core.shared.fields.PositiveDecimalField(max_digits=10, decimal_places=2, verbose_name='total area'),
        ),
    ]
