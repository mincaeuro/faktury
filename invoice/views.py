#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

from django.template import Context, loader


def index(request):
	Fakturas_list = Faktura.objects.all()
	t = loader.get_template('invoice/index.html')
	c = Context({'Fakturas_list': Fakturas_list,})
	return HttpResponse(t.render(c))

def detail(request, faktura_id):
	Fakturas_list = Faktura.objects.all()
	t = loader.get_template('invoice/index.html')
	c = Context({'Fakturas_list': Fakturas_list,})
	return HttpResponse(t.render(c))