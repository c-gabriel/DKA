from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    path('', views.index, name='index'),
#    path('', views.busca, name='busca'),
#    path('', views.dicionario, name='dicionario'),
#    path('', views.sobre, name='sobre'),
#    path('', views.contato, name='contato'),

    url(r'^dicionario/$', views.dicionario, name='dicionario'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^busca/$', views.busca, name='busca'),
#    url(r'^$', views.word_list, name='word_list'),
]
