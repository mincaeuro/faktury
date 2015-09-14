from django.db import models
import uuid
# Create your models here.


class Login(models.Model):
	id = models.AutoField(primary_key=True, blank=False)
	user = models.CharField(blank=False, unique=True, max_length=50)
	email = models.EmailField(blank=False)
	password = models.CharField(blank=False, max_length=150)
	def __unicode__(self):
		return str(self.user)

class Odosielatel(models.Model):
	id = models.AutoField(primary_key=True, blank=False)
	creator = models.ForeignKey(Login, blank=False)
	nazov = models.CharField(blank=False, max_length=200)
	meno = models.CharField(blank=False, max_length=50)
	priezvisko = models.CharField(blank=False, max_length=50)
	ico = models.CharField(blank=False, max_length=50)
	dic = models.CharField(blank=False, max_length=50)
	banka = models.CharField(blank=False, max_length=100)
	cislo_uctu = models.CharField(blank=False, max_length=100)
	platca_DPH = models.CharField(choices=[("a", "ano"),("n", "nie")], max_length=1)
	telefon = models.CharField(max_length=50)
	adresa_ulica = models.CharField(max_length=200)
	adresa_mesto = models.CharField(max_length=90)
	adresa_PSC = models.CharField(max_length=20)
	def __unicode__(self):
		return str(self.nazov)
	
class Odberatel(models.Model):
	id = models.AutoField(primary_key=True)
	owner = models.ForeignKey(Login, blank=False)
	nazov = models.CharField(blank=True, max_length=200)
	meno = models.CharField(blank=True, max_length=50)
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
	def __unicode__(self):
		return str(self.nazov)
	
class Faktura(models.Model):
	id = models.AutoField(primary_key=True)
	owner = models.ForeignKey(Login, blank=False)
	creator = models.ForeignKey(Odosielatel, blank=False)
	cislo_faktury = models.CharField(blank=False, max_length=150)
	datum_vystavenia = models.DateField(blank=False)
	datum_splatnosti = models.DateField(blank=False)
	datum_dodania = models.DateField(blank=False)
	konstantny_symbol = models.CharField(blank=False, max_length=150)
	doprava = models.CharField(blank=True, max_length=150)
	komentar = models.TextField(max_length=3000)
	def __unicode__(self):
		return str(self.cislo_faktury)
	
	
class Polozky(models.Model):
	id = models.AutoField(primary_key=True)
	owner = models.ForeignKey(Login, blank=False)
	faktura = models.ForeignKey(Faktura, blank=False)
	nazov = models.CharField(blank=False, max_length=300)
	mnozstvo = models.CharField(blank=False, max_length=100)
	cena = models.CharField(blank=False, max_length=100)
	def __unicode__(self):
		return str(self.nazov)


