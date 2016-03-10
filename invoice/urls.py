from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^firma/$', views.firmas_all, name='firmas_all'),
	url(r'^zakaznici/$', views.zakaznik_all, name='zakaznik_all'),
	url(r'^faktury/$', views.faktury_all, name='faktury_all'),
	url(r'^detail/(?P<faktura_id>\d+)/$', views.detail, name='detail'),
	url(r'^detail/(?P<faktura_id>\d+)/edit/$', views.edit_detail, name='edit_detail'),
	url(r'^firma/(?P<firma_id>\d+)/$', views.firma, name='firma'),
	url(r'^zakaznik/(?P<zakaznik_id>\d+)/$', views.zakaznik, name='zakaznik'),
	url(r'^login/$', views.index, name='index'),
]
