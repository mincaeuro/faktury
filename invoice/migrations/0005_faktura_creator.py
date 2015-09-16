# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20150914_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='faktura',
            name='creator',
            field=models.ForeignKey(default=datetime.datetime(2015, 9, 14, 14, 48, 9, 559810, tzinfo=utc), to='invoice.Login'),
            preserve_default=False,
        ),
    ]
