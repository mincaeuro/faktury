# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20150911_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faktura',
            name='owner',
            field=models.ForeignKey(to='invoice.Odberatel'),
        ),
    ]
