# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_tagsmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='tags',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.TagsModel', verbose_name='文章标签'),
        ),
    ]
