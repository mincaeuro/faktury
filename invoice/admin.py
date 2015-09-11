from django.contrib import admin

from .models import *

class ChoiceInline(admin.TabularInline):
	model = Polozky
	extra = 1

class LoginAdm(admin.ModelAdmin):
    fieldsets = [
		('Udaje uzivatela', {'fields': ['user','nazov', 'meno', 'priezvisko', 'email', 'telefon', 'ico', 'dic', 'platca_DPH']}),
		('Adresa', {'fields': ['adresa_ulica', 'adresa_mesto', 'adresa_PSC'], 'classes': ['collapse']}),
		('Bankove spojenie', {'fields': ['banka', 'cislo_uctu'], 'classes': ['collapse']}),

				]
# !!! this seams to not work :/

#class PolozkyAdm(admin.ModelAdmin):
#	fieldsets = [
#				 ('Polozky Faktury'), {'fields': ['faktura']}
#				 ('Zoznam poloziek'), {'fields': ['nazov', 'mnozstvo', 'cena']}
#				
#				]
#	inlines = [ChoiceInline]

admin.site.register(Login, LoginAdm)
admin.site.register(Faktura)
admin.site.register(Polozky)#, PolozkyAdm)
admin.site.register(Odberatel)
