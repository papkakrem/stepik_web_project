# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0006_auto_20170911_0619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={},
        ),
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(null=True),
        ),
    ]