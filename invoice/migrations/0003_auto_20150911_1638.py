# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20150911_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faktura',
            name='owner',
            field=models.ForeignKey(to='invoice.Login'),
        ),
        migrations.AlterField(
            model_name='odberatel',
            name='owner',
            field=models.ForeignKey(to='invoice.Login'),
        ),
        migrations.AlterField(
            model_name='polozky',
            name='faktura',
            field=models.ForeignKey(to='invoice.Faktura'),
        ),
    ]
