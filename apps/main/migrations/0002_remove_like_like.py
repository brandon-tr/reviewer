# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-24 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
    ]