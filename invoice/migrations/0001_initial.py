# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faktura',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cislo_faktury', models.CharField(max_length=150)),
                ('datum_vystavenia', models.DateField()),
                ('datum_splatnosti', models.DateField()),
                ('datum_dodania', models.DateField()),
                ('konstantny_symbol', models.CharField(max_length=150)),
                ('doprava', models.CharField(max_length=150, blank=True)),
                ('komentar', models.TextField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('user', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('nazov', models.CharField(max_length=200)),
                ('meno', models.CharField(max_length=50)),
                ('priezvisko', models.CharField(max_length=50)),
                ('ico', models.CharField(max_length=50)),
                ('dic', models.CharField(max_length=50)),
                ('banka', models.CharField(max_length=100)),
                ('cislo_uctu', models.CharField(max_length=100)),
                ('platca_DPH', models.CharField(max_length=1, choices=[(b'a', b'ano'), (b'n', b'nie')])),
                ('telefon', models.CharField(max_length=50)),
                ('adresa_ulica', models.CharField(max_length=200)),
                ('adresa_mesto', models.CharField(max_length=90)),
                ('adresa_PSC', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Odberatel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nazov', models.CharField(max_length=200, blank=True)),
                ('meno', models.CharField(max_length=50, blank=True)),
                ('priezvisko', models.CharField(max_length=50, blank=True)),
                ('adresa_ulica', models.CharField(max_length=200)),
                ('adresa_mesto', models.CharField(max_length=90)),
                ('adresa_psc', models.CharField(max_length=20)),
                ('ico', models.CharField(max_length=50)),
                ('dic', models.CharField(max_length=50)),
                ('icdph', models.CharField(max_length=50)),
                ('banka', models.CharField(max_length=100)),
                ('cislo_uctu', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(default=uuid.uuid4, to='invoice.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Polozky',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nazov', models.CharField(max_length=300)),
                ('mnozstvo', models.CharField(max_length=100)),
                ('cena', models.CharField(max_length=100)),
                ('faktura', models.ForeignKey(default=uuid.uuid4, to='invoice.Faktura')),
            ],
        ),
        migrations.AddField(
            model_name='faktura',
            name='owner',
            field=models.ForeignKey(default=uuid.uuid4, to='invoice.Login'),
        ),
    ]
