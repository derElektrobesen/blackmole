# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moleimage',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='moleimage',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]