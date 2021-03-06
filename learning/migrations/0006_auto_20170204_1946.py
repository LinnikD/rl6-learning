# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_userresult_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='\u0410\u043a\u0442\u0438\u0432\u0435\u043d \u0441\u0435\u0439\u0447\u0430\u0441?'),
        ),
        migrations.AlterField(
            model_name='test',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Discipline', verbose_name='\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0430'),
        ),
    ]
