# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-09 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0002_auto_20180609_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tag',
        ),
    ]