from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^firma/$', views.firmas_all, name='firmas_all'),
	url(r'^detail/(?P<faktura_id>\d+)/$', views.detail, name='detail'),
	url(r'^firma/(?P<firma_id>\d+)/$', views.firma, name='firma'),
]