from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^$', views.word_list, name='word_list'),
]
