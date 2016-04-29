# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 14:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mood', '0022_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mood.Day'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
