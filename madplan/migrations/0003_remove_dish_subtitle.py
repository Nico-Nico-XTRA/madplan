# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madplan', '0002_dish_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='subtitle',
        ),
    ]
