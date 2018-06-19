# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-11 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20180611_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='IP',
        ),
        migrations.AlterField(
            model_name='hosts',
            name='IP',
            field=models.GenericIPAddressField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='system',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]