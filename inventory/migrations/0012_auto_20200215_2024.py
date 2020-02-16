# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-16 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_equipmentuserguide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentuserguide',
            name='file',
            field=models.FileField(storage=inventory.models.DocStorage(), upload_to=inventory.models.guide_file_name),
        ),
    ]
