# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-25 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_like_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='cat',
        ),
        migrations.AddField(
            model_name='cat',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
