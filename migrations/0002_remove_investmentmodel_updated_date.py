# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-15 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investmentmodel',
            name='updated_date',
        ),
    ]
