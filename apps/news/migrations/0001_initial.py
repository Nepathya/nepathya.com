# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('source', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
