# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0011_event_subject'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Subject',
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_time']},
        ),
    ]