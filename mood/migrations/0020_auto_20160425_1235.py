# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0019_auto_20160410_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='show',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(),
        ),
    ]
