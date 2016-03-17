# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 16:57
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mosaico', '0007_auto_20160220_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='template_path',
        ),
        migrations.AddField(
            model_name='template',
            name='template_data',
            field=jsonfield.fields.JSONField(default='{}'),
            preserve_default=False,
        ),
    ]
