# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-04 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20180604_1118'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
