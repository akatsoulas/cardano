# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vouched', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('name', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'get_latest_by': 'created',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Mozillian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vouched', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'get_latest_by': 'created',
                'ordering': ['-created'],
            },
        ),
    ]
