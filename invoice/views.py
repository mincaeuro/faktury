from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
from .models import *



def index(request):
	Fakturas_list = Faktura.objects.all()
	t = loader.get_template('invoice/index.html')
	c = Context({'Fakturas_list': Fakturas_list,})
	return HttpResponse(t.render(c))

def detail(request, faktura_id):
	faktura = get_object_or_404(Faktura, pk=faktura_id)
	return render(request, 'invoice/details.html', {'faktura': faktura})

def firmas_all(request):
	Firmas_list = Firma.objects.all()
	t = loader.get_template('invoice/firmas.html')
	c = Context({'Firmas_list': Firmas_list,})
	return HttpResponse(t.render(c))

def zakaznik_all(request):
	zakaznik_list = Zakaznik.objects.all()
	t = loader.get_template('invoice/zakaznici.html')
	c = Context({'zakaznik_list': zakaznik_list,})
	return HttpResponse(t.render(c))

def firma(request, firma_id):
	firma = get_object_or_404(Firma, pk=firma_id)
	return render(request, 'invoice/firma.html', {'firma': firma})

def edit_detail(request, faktura_id):
	faktura = get_object_or_404(Faktura, pk=faktura_id)
	try:
		zmeny = faktura.cislo_faktury.get(pk=request.POST['komentar'])
    	except (KeyError, Faktura.DoesNotExist):
    	# Redisplay the question voting form.
			return render(request, 'invoice/details.html#letsedit', {
            'faktura': faktura,
						'error_message': "Chyba, ne-existujuci/neaktualny zaznam",
        })
	else:
				zmeny.edit_details += 1
				zmeny.save()
	return HttpResponseRedirect(reverse('faktura:faktura', args=(faktura.id,)))