# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 09:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0024_auto_20170213_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='api_key',
        ),
    ]