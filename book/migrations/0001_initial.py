# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField(verbose_name='Текст')),
                ('published', models.BooleanField(default=False)),
                ('publish', models.DateField(verbose_name='Дата публикации')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Время пуликации')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]
