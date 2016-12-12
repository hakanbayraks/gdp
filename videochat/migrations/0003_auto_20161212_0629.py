# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-12 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videochat', '0002_auto_20150610_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_status',
            field=models.CharField(choices=[(b'Initialize', b'Initializing'), (b'Active', b'Active'), (b'Waiting', b'Waiting'), (b'Terminated', b'Terminated')], default=b'Initialize', max_length=10),
        ),
        migrations.AlterField(
            model_name='chat',
            name='chatname',
            field=models.CharField(max_length=100),
        ),
    ]
