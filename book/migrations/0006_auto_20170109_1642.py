# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-09 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import djorm_pgfulltext.fields


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20170109_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(db_index=True, default='', editable=False, null=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='content',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=256, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
    ]