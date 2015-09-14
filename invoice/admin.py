from django.contrib import admin

from .models import *

class PolozkyInline(admin.TabularInline):
	model = Polozky
	extra = 1
	
class OdberatelInline(admin.TabularInline):
	model = Faktura
	
class LoginInline(admin.TabularInline):
	model = Faktura
	extra = 0
	
	

class LoginAdm(admin.ModelAdmin):
	fieldsets = [
		('Udaje uzivatela', {'fields': ['user','nazov', 'meno', 'priezvisko', 'email', 'telefon', 'ico', 'dic', 'platca_DPH']}),
		('Adresa', {'fields': ['adresa_ulica', 'adresa_mesto', 'adresa_PSC']}),
		('Bankove spojenie', {'fields': ['banka', 'cislo_uctu']}),
				]
	inlines = [LoginInline]

class PolozkyAdm(admin.ModelAdmin):
	fieldsets = [
				 ('Cislo Faktury', {'fields': ['cislo_faktury']}),
				 ('Udaje', {'fields': ['datum_vystavenia', 'datum_splatnosti', 'datum_dodania', 'konstantny_symbol', 'doprava', 'komentar']}),
				]
	inlines = [PolozkyInline]

class OdberatelAdm(admin.ModelAdmin):
	fieldsets = [
		('Udaje odberatela', {'fields': ['nazov', 'meno', 'priezvisko', 'email', 'telefon', 'ico', 'dic', 'icdph']}),
		('Adresa', {'fields': ['adresa_ulica', 'adresa_mesto', 'adresa_psc']}),
		('Bankove spojenie', {'fields': ['banka', 'cislo_uctu']}),
				]
	#inlines = [OdberatelInline]
	
admin.site.register(Login, LoginAdm)
admin.site.register(Faktura, PolozkyAdm)
admin.site.register(Polozky)
admin.site.register(Odberatel, OdberatelAdm)
