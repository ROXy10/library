# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-09 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Опобликовано'),
        ),
    ]
