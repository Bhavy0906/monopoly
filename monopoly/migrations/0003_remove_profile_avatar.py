# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-03-20 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monopoly', '0002_auto_20210320_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]
