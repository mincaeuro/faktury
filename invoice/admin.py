from django.contrib import admin

from .models import *

class PolozkyInline(admin.TabularInline):
	model = Polozky
	extra = 1
	
class ZakaznikInline(admin.TabularInline):
	model = Faktura
	extra = 0

class FirmaInline(admin.TabularInline):
	model = Zakaznik
	extra = 0
	
class LoginInline(admin.StackedInline):
	model = Firma
	extra = 0
	
class FakturaInline(admin.TabularInline):
	model = Polozky
	extra = 1

class LoginAdm(admin.ModelAdmin):
	fieldsets = [
		('Prihlasovacie Udaje', {'fields': ['user','email', 'password']}),
				]
	inlines = [LoginInline]
	list_display = ('user', 'email')
	list_filter = ['user']
	search_fields = ['nazov']

class FirmaAdm(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['creator']}),
		('Udaje Firmy', {'fields': ['nazov', 'meno', 'priezvisko', 'telefon', 'ico', 'dic', 'platca_DPH']}),
		('Adresa', {'fields': ['adresa_ulica', 'adresa_mesto', 'adresa_PSC']}),
		('Bankove spojenie', {'fields': ['banka', 'cislo_uctu']}),
				]
	inlines = [FirmaInline]
	list_display = ('nazov', 'meno', 'telefon')
	list_filter = ['nazov']
	search_fields = ['nazov']

class FakturaAdm(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['owner']}),
		('Firma', {'fields': ['creator']}), 
		('Zakaznik', {'fields': ['created_for']}), 
		('Cislo Faktury', {'fields': ['cislo_faktury']}),
		('Udaje', {'fields': ['datum_vystavenia', 'datum_splatnosti', 'datum_dodania', 'konstantny_symbol', 'doprava', 'komentar']}),
				]
	inlines = [FakturaInline]
	list_display = ('cislo_faktury', 'datum_vystavenia', 'created_for')
	list_filter = ['cislo_faktury']
	search_fields = ['nazov']

class ZakaznikAdm(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['owner']}),
		('Firma', {'fields': ['creator']}),
		('Udaje Zakaznika', {'fields': ['nazov', 'meno', 'priezvisko', 'email', 'telefon', 'ico', 'dic', 'icdph']}),
		('Adresa', {'fields': ['adresa_ulica', 'adresa_mesto', 'adresa_psc']}),
		('Bankove spojenie', {'fields': ['banka', 'cislo_uctu']}),
				]
	inlines = [ZakaznikInline]
	list_display = ('nazov', 'meno', 'email')
	list_filter = ['nazov']
	search_fields = ['nazov']

class PolozkyAdm(admin.ModelAdmin):
	list_display = ('nazov', 'mnozstvo', 'cena', 'faktura', 'owner')
	list_filter = ['nazov']
	search_fields = ['nazov']
	
admin.site.register(Login, LoginAdm)
admin.site.register(Zakaznik, ZakaznikAdm)
admin.site.register(Firma, FirmaAdm)
admin.site.register(Faktura, FakturaAdm)
admin.site.register(Polozky, PolozkyAdm)

