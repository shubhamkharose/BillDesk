# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0007_auto_20171027_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='guestBill_Inven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='guestBilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saletime', models.DateTimeField(auto_now_add=True)),
                ('tot_price', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='guestCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('c_name', models.CharField(max_length=100)),
                ('age_group', models.IntegerField()),
                ('village', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('gst_in', models.CharField(default=b'', max_length=15)),
                ('del_flag', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['c_name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='guestInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('i_name', models.CharField(max_length=100)),
                ('i_price', models.IntegerField(default=0)),
                ('gst_perc', models.IntegerField(default=0)),
                ('del_flag', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['i_name'],
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='onk_rbill_inven',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='onk_rbilling',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='onk_rcustomer',
            options={'managed': False, 'ordering': ['c_name']},
        ),
        migrations.AlterModelOptions(
            name='onk_rinventory',
            options={'managed': False, 'ordering': ['i_name']},
        ),
        migrations.AddField(
            model_name='guestbilling',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.guestCustomer'),
        ),
        migrations.AddField(
            model_name='guestbill_inven',
            name='Billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.guestBilling'),
        ),
        migrations.AddField(
            model_name='guestbill_inven',
            name='Inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.guestInventory'),
        ),
    ]
