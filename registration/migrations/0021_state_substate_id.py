# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_auto_20160504_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='SubState_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.SubState', verbose_name='\u0414\u04af\u04af\u0440\u044d\u0433/\u0421\u0443\u043c'),
            preserve_default=False,
        ),
    ]
