# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-26 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20171126_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pasword',
            new_name='password',
        ),
    ]
