# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-01 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171001_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predio',
            name='off',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='on',
        ),
    ]