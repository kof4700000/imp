# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-24 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180522_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='impuser',
            name='display_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
