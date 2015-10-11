# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cover_photo', filebrowser.fields.FileBrowseField(max_length=500, null=True, verbose_name='cover photo', blank=True)),
                ('square', models.PositiveIntegerField(verbose_name='square')),
                ('deadline', models.PositiveIntegerField(null=True, verbose_name='deadline', blank=True)),
                ('is_delivered', models.BooleanField(default=False, verbose_name='is delivered')),
                ('price', models.PositiveIntegerField(null=True, verbose_name='price', blank=True)),
                ('your_commission', models.PositiveIntegerField(null=True, verbose_name='your commission', blank=True)),
            ],
            options={
                'verbose_name': 'assignation',
                'verbose_name_plural': 'assignations',
            },
        ),
        migrations.CreateModel(
            name='AssignationAdditionalPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('photo', filebrowser.fields.FileBrowseField(max_length=500, null=True, verbose_name='photo', blank=True)),
                ('assignation', models.ForeignKey(verbose_name='assignation', to='immovables.Assignation', related_name='additional_photos')),
            ],
            options={
                'verbose_name': 'assignation additional photo',
                'verbose_name_plural': 'assignation additional photos',
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'developer',
                'verbose_name_plural': 'developers',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
                'verbose_name': 'district',
                'verbose_name_plural': 'districts',
            },
        ),
        migrations.CreateModel(
            name='FlatType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'flat type',
                'verbose_name_plural': 'flat types',
            },
        ),
        migrations.CreateModel(
            name='HousingEstate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('cover_photo', filebrowser.fields.FileBrowseField(max_length=500, null=True, verbose_name='cover photo', blank=True)),
                ('address', models.TextField(verbose_name='address')),
                ('deadline', models.PositiveIntegerField(null=True, verbose_name='deadline', blank=True)),
                ('is_delivered', models.BooleanField(default=False, verbose_name='is delivered')),
                ('developer', models.ForeignKey(verbose_name='developer', null=True, to='immovables.Developer', blank=True)),
                ('district', models.ForeignKey(verbose_name='district', null=True, to='immovables.District', blank=True)),
                ('subway_station', models.ForeignKey(verbose_name='subway station', null=True, to='subway.Station', blank=True)),
            ],
            options={
                'verbose_name': 'housing estate',
                'verbose_name_plural': 'housing estates',
            },
        ),
        migrations.CreateModel(
            name='HousingEstateAdditionalPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('photo', filebrowser.fields.FileBrowseField(max_length=500, null=True, verbose_name='photo', blank=True)),
                ('housing_estate', models.ForeignKey(verbose_name='housing estate', to='immovables.HousingEstate', related_name='additional_photos')),
            ],
            options={
                'verbose_name': 'housing estate additional photo',
                'verbose_name_plural': 'housing estate additional photos',
            },
        ),
        migrations.AddField(
            model_name='assignation',
            name='flat_type',
            field=models.ForeignKey(verbose_name='flat type', to='immovables.FlatType'),
        ),
        migrations.AddField(
            model_name='assignation',
            name='housing_estate',
            field=models.ForeignKey(verbose_name='housing estate', null=True, to='immovables.HousingEstate', blank=True),
        ),
    ]
