# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interchange',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'interchanges',
                'verbose_name': 'interchange',
            },
        ),
        migrations.AlterOrderWithRespectTo(
            name='station',
            order_with_respect_to='branch',
        ),
        migrations.AddField(
            model_name='interchange',
            name='from_station',
            field=models.ForeignKey(to='subway.Station', related_name='interchanges', verbose_name='from station'),
        ),
        migrations.AddField(
            model_name='interchange',
            name='to_station',
            field=models.ForeignKey(to='subway.Station', related_name='+', verbose_name='to station'),
        ),
    ]
