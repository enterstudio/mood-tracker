# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0018_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
