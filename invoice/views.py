from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from decimal import Decimal

# Create your views here.
from .models import *
from .forms import LoginForm


def index(request):
    Fakturas_list = Faktura.objects.all()
    Login_list = Login.objects.all()
    sucet_list = Polozky.objects.all()#.aggregate(total=Sum(F('mnozstvo') * F('cena')))['total']
    return render(request, 'invoice/index.html',
                  {'Fakturas_list': Fakturas_list, 'Login_list': Login_list, 'form': LoginForm, 'sucet_list': sucet_list})


####custom login - not in use

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = User.objects.get(email=form.cleaned_data['email'])
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'invoice/index.html',
                                  {'Fakturas_list': Fakturas_list, 'Login_list': Login_list})
            else:
                form = LoginForm(request.POST or None)
            return HttpResponseRedirect('/?there_you_go')
    else:
        form = LoginForm(request.POST or None)
    return HttpResponseRedirect('/?no_login_requested')


@login_required(login_url='/logmein/')
def detail(request, faktura_id):
    faktura = get_object_or_404(Faktura, pk=faktura_id)
    polozky = Polozky.objects.filter(faktura=faktura_id)
    # zakaznik = Zakaznik.objects.filter(faktura=faktura.db_uuid)
    zakaznik = Zakaznik.objects.get(faktura=faktura.id)
    sucet = Polozky.objects.filter(faktura=faktura_id).aggregate(total=Sum(F('mnozstvo') * F('cena')))['total']
    t = 'invoice/details.html'
    c = {'faktura': faktura, 'polozky': polozky, 'zakaznik': zakaznik, 'sucet': sucet}
    return HttpResponse(render_to_string(t, c))


@login_required(login_url='/logmein/')
def firmas_all(request):
    Firmas_list = Firma.objects.all()
    t = 'invoice/firmas.html'
    c = {'Firmas_list': Firmas_list, }
    return HttpResponse(render_to_string(t, c))


@login_required(login_url='/logmein/')
def zakaznik_all(request):
    zakaznik_list = Zakaznik.objects.all()
    t = 'invoice/zakaznici.html'
    c = {'zakaznik_list': zakaznik_list, }
    return HttpResponse(render_to_string(t, c))


@login_required(login_url='/logmein/')
def faktury_all(request):
    Fakturas_list = Faktura.objects.all()
    t = 'invoice/faktury.html'
    c = {'Fakturas_list': Fakturas_list, }
    return HttpResponse(render_to_string(t, c))


@login_required(login_url='/logmein/')
def firma(request, firma_id):
    firma = get_object_or_404(Firma, pk=firma_id)
    zoznam = Faktura.objects.filter(creator=firma.id)
    t = 'invoice/firma.html'
    c = {'firma': firma, 'zoznam': zoznam}
    return HttpResponse(render_to_string(t, c))


@login_required(login_url='/logmein/')
def zakaznik(request, zakaznik_id):
    zakaznik = get_object_or_404(Zakaznik, pk=zakaznik_id)
    zoznam = Faktura.objects.filter(created_for=zakaznik.id)
    t = 'invoice/zakaznik.html'
    c = {'zakaznik': zakaznik, 'zoznam': zoznam}
    return HttpResponse(render_to_string(t, c))


@login_required(login_url='/logmein/')
def edit_detail(request, faktura_id):
    faktura = get_object_or_404(Faktura, pk=faktura_id)
    try:
        zmeny = faktura.cislo_faktury.get(pk=request.POST['komentar'])
    except(KeyError, Faktura.DoesNotExist):
        return render(request, 'invoice/details.html#letsedit', {
            'faktura': faktura, 'error_message': "Chyba, ne-existujuci/neaktualny zaznam",
        })
    else:
        zmeny.edit_details += 1
        zmeny.save()
    return HttpResponseRedirect(reverse('faktura:faktura', args=(faktura.id,)))
