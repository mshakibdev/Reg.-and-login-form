# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='your_name',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
