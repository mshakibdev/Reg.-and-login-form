# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0003_myuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='your_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
