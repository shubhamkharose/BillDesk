# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 09:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0011_auto_20171028_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samrbilling',
            name='saletime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
