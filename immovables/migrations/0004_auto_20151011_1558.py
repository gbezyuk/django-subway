# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.shared.fields


class Migration(migrations.Migration):

    dependencies = [
        ('immovables', '0003_auto_20151011_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignation',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='assignation',
            name='is_delivered',
        ),
        migrations.AlterField(
            model_name='assignation',
            name='kitchen_area',
            field=core.shared.fields.PositiveDecimalField(null=True, blank=True, verbose_name='kitchen area', decimal_places=2, max_digits=10),
        ),
    ]
