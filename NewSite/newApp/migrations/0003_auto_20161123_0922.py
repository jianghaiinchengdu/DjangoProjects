# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-23 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0002_testmodel_param4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='param3',
            field=models.DateTimeField(auto_now=True, verbose_name='sss'),
        ),
    ]
