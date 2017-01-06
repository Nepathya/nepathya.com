# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-30 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0006_auto_20160822_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='discography.Album'),
        ),
    ]