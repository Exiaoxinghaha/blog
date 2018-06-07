# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180518_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=10, null=True, verbose_name='类别标签')),
            ],
            options={
                'verbose_name': '类别标签',
                'verbose_name_plural': '类别标签',
            },
        ),
    ]
