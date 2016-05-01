# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 14:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0023_auto_20160429_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mood.Day'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]