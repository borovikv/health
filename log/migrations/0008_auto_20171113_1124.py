# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0007_auto_20171113_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]