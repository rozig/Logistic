# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20160417_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='Indication_ID',
            field=models.ManyToManyField(blank=True, null=True, to='registration.Indication', verbose_name='\u0428\u0438\u043d\u0436 \u0447\u0430\u043d\u0430\u0440'),
        ),
    ]
