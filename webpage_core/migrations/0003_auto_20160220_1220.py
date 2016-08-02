# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0002_page_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pages',
            field=models.ManyToManyField(blank=True, null=True, related_name='contents', to='webpage_core.Page'),
        ),
    ]