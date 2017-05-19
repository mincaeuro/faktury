# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 11:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20170519_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='cislo_uctu',
            field=models.CharField(max_length=24, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Zadajte cislo vo formate IBAN')]),
        ),
    ]
