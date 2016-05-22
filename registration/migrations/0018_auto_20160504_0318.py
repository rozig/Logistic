# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_delivery_recipient_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubState',
            fields=[
                ('SubState_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='\u0421\u0443\u043c/\u0434\u04af\u04af\u0440\u0433\u0438\u0439\u043d \u0434\u0443\u0433\u0430\u0430\u0440')),
                ('SubState', models.CharField(max_length=45, verbose_name='\u0421\u0443\u043c/\u0434\u04af\u04af\u0440\u0433\u0438\u0439\u043d \u043d\u044d\u0440')),
            ],
            options={
                'verbose_name': '\u0421\u0443\u043c/\u0434\u04af\u04af\u0440\u044d\u0433',
            },
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='Delivery_From_Address',
        ),
        migrations.AddField(
            model_name='delivery',
            name='State_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.State', verbose_name='\u0425\u043e\u0442/\u0410\u0439\u043c\u0430\u0433'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='SubState_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.SubState', verbose_name='\u0414\u04af\u04af\u0440\u044d\u0433/\u0421\u0443\u043c'),
            preserve_default=False,
        ),
    ]