from django.conf.urls import url
from . import views
from django.urls import path

#app_name = 'dicionario'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('dicionario/', views.dicionario, name='dicionario'),
	path('sobre/', views.sobre, name='sobre'),
	path('contato/', views.contato, name='contato'),
	path('busca/', views.busca, name='busca'),
	path('dicionario/pt/', views.pt, name='pt'),
    path('dicionario/en/', views.en, name='en'),
    path('dicionario/cr/', views.cr, name='cr'),
	url(r'^search/$', views.search),
    path('dicionario/pt/<q>/', views.word_list_pt, name='word_list_pt'),
	path('dicionario/en/<q>/', views.word_list_en, name='word_list_en'),
	path('dicionario/cr/<q>/', views.word_list_cr, name='word_list_cr'),
]
