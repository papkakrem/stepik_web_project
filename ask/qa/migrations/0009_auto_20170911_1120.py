# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0008_auto_20170911_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
