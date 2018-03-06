from django.urls import path

from . import views

app_name = 'invoice'
urlpatterns = [
	path('', views.index, name='index'),
	path('firma/', views.firmas_all, name='firmas_all'),
	path('zakaznici/', views.zakaznik_all, name='zakaznik_all'),
	path('logmein/', views.log_in, name='log_in'),
	path('faktury/', views.faktury_all, name='faktury_all'),
	path('detail/<int:faktura_id>/	', views.detail, name='detail'),
	path('detail/<int:faktura_id>/edit/', views.edit_detail, name='edit_detail'),
	path('firma/<int:firma_id>/', views.firma, name='firma'),
	path('zakaznik/<int:zakaznik_id>/', views.zakaznik, name='zakaznik'),
	path('kontakt/', views.kontakt, name='kontakt'),

]
