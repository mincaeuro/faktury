from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout



# Create your views here.
from .models import *
from .forms import LoginForm

def log_in(request):
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
	return render_to_response('invoice/login.html', form=RequestContext(request))


def index(request):
	Fakturas_list = Faktura.objects.all()
	Login_list = Login.objects.all()
	t = loader.get_template('invoice/index.html')
	c = Context({'Fakturas_list': Fakturas_list, 'Login_list': Login_list})
	return HttpResponse(t.render(c))

def login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=user, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required(login_url='/logmein/')
def detail(request, faktura_id):
	faktura = get_object_or_404(Faktura, pk=faktura_id)
	polozky = Polozky.objects.filter(faktura=faktura_id)
	#zakaznik = Zakaznik.objects.filter(faktura=faktura.db_uuid)
	zakaznik = Zakaznik.objects.get(faktura=faktura.id)
	t = loader.get_template('invoice/details.html')
	c = Context({'faktura': faktura, 'polozky': polozky, 'zakaznik': zakaznik})
	return HttpResponse(t.render(c))

@login_required(login_url='/logmein/')
def firmas_all(request):
	Firmas_list = Firma.objects.all()
	t = loader.get_template('invoice/firmas.html')
	c = Context({'Firmas_list': Firmas_list,})
	return HttpResponse(t.render(c))

@login_required(login_url='/logmein/')
def zakaznik_all(request):
	zakaznik_list = Zakaznik.objects.all()
	t = loader.get_template('invoice/zakaznici.html')
	c = Context({'zakaznik_list': zakaznik_list,})
	return HttpResponse(t.render(c))

@login_required(login_url='/logmein/')
def faktury_all(request):
	Fakturas_list = Faktura.objects.all()
	t = loader.get_template('invoice/faktury.html')
	c = Context({'Fakturas_list': Fakturas_list,})
	return HttpResponse(t.render(c))

@login_required(login_url='/logmein/')
def firma(request, firma_id):
	firma = get_object_or_404(Firma, pk=firma_id)
	zoznam = Faktura.objects.filter(creator=firma.id)
	t = loader.get_template('invoice/firma.html')
	c = Context({'firma': firma, 'zoznam': zoznam})
	return HttpResponse(t.render(c))

@login_required(login_url='/logmein/')
def zakaznik(request, zakaznik_id):
	zakaznik = get_object_or_404(Zakaznik, pk=zakaznik_id)
	zoznam = Faktura.objects.filter(created_for=zakaznik.id)
	t = loader.get_template('invoice/zakaznik.html')
	c = Context({'zakaznik': zakaznik, 'zoznam': zoznam})
	return HttpResponse(t.render(c))

@login_required(login_url='/logmein/')
def edit_detail(request, faktura_id):
	faktura = get_object_or_404(Faktura, pk=faktura_id)
	try:
		zmeny = faktura.cislo_faktury.get(pk=request.POST['komentar'])
	except(KeyError, Faktura.DoesNotExist):
			return render(request, 'invoice/details.html#letsedit', {
				'faktura': faktura,'error_message': "Chyba, ne-existujuci/neaktualny zaznam",
				})
	else:
				zmeny.edit_details += 1
				zmeny.save()
	return HttpResponseRedirect(reverse('faktura:faktura', args=(faktura.id,)))
