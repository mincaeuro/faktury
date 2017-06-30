# -- coding: utf-8
from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.db.models import Sum, F


# Create your models here.


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    db_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.CharField(blank=False, unique=True, max_length=50)
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False, max_length=150)

    def __str__(self):
        return self.user


class Firma(models.Model):
    id = models.AutoField(primary_key=True)
    db_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(Login, blank=False)
    nazov = models.CharField(blank=False, max_length=200)
    meno = models.CharField(blank=False, max_length=50)
    priezvisko = models.CharField(blank=False, max_length=50)
    ico = models.CharField(blank=False, max_length=50)
    dic = models.CharField(blank=False, max_length=50)
    banka = models.CharField(blank=False, max_length=100)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Zadajte cislo vo formate IBAN')
    cislo_uctu = models.CharField(blank=False, max_length=24, validators=[alphanumeric])
    banky = (
        ('', 'vyberte'),
        ('SUBASKBX', 'Všeobecná úverová banka, a. s.'),
        ('GIBASKBX', 'Slovenská sporiteľňa, a. s.'),
        ('TATRSKBX', 'Tatra banka, a. s.'),
        ('BREXSKBX', 'MBANK – BRE Bank SA, pobočka zahraničnej banky mBank v SR'),
        ('UNCRSKBX', 'UniCredit Bank Czech Republic and Slovakia, a. s., pobočka zahr. banky'),
        ('CEKOSKBX', 'ČSOB – Československá obchodná banka, a.s.'),
    )
    cislo_swift = models.CharField(max_length=8, choices=banky, default='', blank=False)
    platca_DPH = models.CharField(choices=[("20", "ano"), ("0", "nie")], max_length=2)
    telefon = models.CharField(max_length=50)
    adresa_ulica = models.CharField(max_length=200)
    adresa_mesto = models.CharField(max_length=90)
    adresa_PSC = models.CharField(max_length=20)

    def __str__(self):
        return self.nazov


class Zakaznik(models.Model):
    id = models.AutoField(primary_key=True)
    db_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Login, blank=False)
    creator = models.ForeignKey(Firma, blank=False)
    nazov = models.CharField(blank=True, max_length=200)
    meno = models.CharField(blank=True, max_length=50)
    cislo = models.CharField(blank=True, max_length=50)
    priezvisko = models.CharField(blank=True, max_length=50)
    adresa_ulica = models.CharField(max_length=200)
    adresa_mesto = models.CharField(max_length=90)
    adresa_psc = models.CharField(max_length=20)
    ico = models.CharField(blank=False, max_length=50)
    dic = models.CharField(blank=False, max_length=50)
    icdph = models.CharField(blank=False, max_length=50)
    banka = models.CharField(blank=False, max_length=100)
    cislo_uctu = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False)
    telefon = models.CharField(max_length=50)

    def __str__(self):
        return self.nazov


class Faktura(models.Model):
    id = models.AutoField(primary_key=True)
    db_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Login, blank=False)
    creator = models.ForeignKey(Firma, blank=False)
    created_for = models.ForeignKey(Zakaznik, blank=False)
    cislo_faktury = models.CharField(blank=False, max_length=10)
    datum_vystavenia = models.DateField(blank=False)
    datum_splatnosti = models.DateField(blank=False)
    datum_dodania = models.DateField(blank=False)
    konstantny_symbol = models.CharField(blank=False, max_length=150)
    doprava = models.CharField(blank=True, max_length=150)
    uhradena = models.CharField(choices=[("1", "ano"), ("0", "nie")], max_length=1, default=0)
    komentar = models.TextField(max_length=3000)

    def __str__(self):
        return self.cislo_faktury


class Polozky(models.Model):
    id = models.AutoField(primary_key=True)
    db_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Login, blank=False)
    faktura = models.ForeignKey(Faktura, blank=False)
    dan = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    nazov = models.CharField(blank=False, max_length=300)
    mnozstvo = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    kod = models.CharField(blank=True, max_length=100)
    cena = models.DecimalField(blank=False, max_digits=20, decimal_places=2)

    def spolu(self):
        return self.mnozstvo * self.cena

    spocitaj = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.nazov
