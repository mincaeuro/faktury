#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, faktura_id):
	return HttpResponse("You're looking at Faktura: %s." % faktura_id)

def firma(request, firma_id):
	return HttpResponse("You're looking at Firma: %s." % firma_id)

def zakaznik(request, zakaznik_id):
	return HttpResponse("You're looking at Zakaznik: %s." % zakaznik_id)

def produkt(request, produkt_id):
	return HttpResponse("You're looking at Produkt: %s." % produkt_id)