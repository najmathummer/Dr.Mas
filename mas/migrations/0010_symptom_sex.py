# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-08 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mas', '0009_disease_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='sex',
            field=models.CharField(default='', max_length=10),
        ),
    ]
