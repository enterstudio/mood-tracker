# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 05:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0012_auto_20160324_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]