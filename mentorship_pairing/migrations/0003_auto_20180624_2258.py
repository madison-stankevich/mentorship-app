# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-24 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship_pairing', '0002_auto_20180604_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pairing',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('rejected', 'Rejected'), ('discontinued', 'Discontinued')], default='pending', max_length=40),
        ),
    ]
