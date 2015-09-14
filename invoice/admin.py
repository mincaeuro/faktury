from django.contrib import admin

from .models import *

class PolozkyInline(admin.TabularInline):
	model = Faktura
	extra = 1
	
class OdberatelInline(admin.TabularInline):
	model = Login
	extra = 0

class OdosielatelInline(admin.TabularInline):
	model = Faktura
	extra = 0
	
class LoginInline(admin.StackedInline):
	model = Odberatel
	extra = 0
	
class FakturaInline(admin.TabularInline):
	model = Polozky
	extra = 1


class LoginAdm(admin.ModelAdmin):
	fieldsets = [
		('Prihlasovacie Udaje', {'fields': ['user','email', 'password']}),
				]
	inlines = [LoginInline]

class OdosielatelAdm(admin.ModelAdmin):
	fieldsets = [
		('Osobne Udaje', {'fields': ['nazov', 'meno', 'priezvisko', 'telefon', 'ico', 'dic', 'platca_DPH']}),
		('Adresa', {'fields': ['adresa_ulica', 'adresa_mesto', 'adresa_PSC']}),
		('Bankove spojenie', {'fields': ['banka', 'cislo_uctu']}),
				]
	#inlines = [OdberatelInline]

class PolozkyAdm(admin.ModelAdmin):
	fieldsets = [
				 ('Cislo Faktury', {'fields': ['cislo_faktury']}),
				 ('Udaje', {'fields': ['datum_vystavenia', 'datum_splatnosti', 'datum_dodania', 'konstantny_symbol', 'doprava', 'komentar']}),
				]
	#inlines = [FakturaInline]

class OdberatelAdm(admin.ModelAdmin):
	fieldsets = [
		('Udaje odberatela', {'fields': ['nazov', 'meno', 'priezvisko', 'email', 'telefon', 'ico', 'dic', 'icdph']}),
		('Adresa', {'fields': ['adresa_ulica', 'adresa_mesto', 'adresa_psc']}),
		('Bankove spojenie', {'fields': ['banka', 'cislo_uctu']}),
				]
	#inlines = [OdberatelInline]
	
admin.site.register(Login, LoginAdm)
admin.site.register(Odberatel, OdberatelAdm)
admin.site.register(Odosielatel)
admin.site.register(Faktura, PolozkyAdm)
admin.site.register(Polozky)

