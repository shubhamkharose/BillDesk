# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-27 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Authority_Admin',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Authority_Customer',
        ),
    ]
